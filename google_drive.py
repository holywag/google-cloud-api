import os.path
from hashlib import sha256
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload

class GoogleDriveApi:
    """Wrapper for driver service of Google Cloud API.
    Google Drive functionality:
        - list all directories
        - upload a file to a given directory
        - set file permissions
    """


    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path


    def init_service(self, scopes):
        token_file_name = 'token_{}.json'.format(sha256(",".join(scopes).encode()).hexdigest())
        creds = None

        if os.path.exists(token_file_name):
            creds = Credentials.from_authorized_user_file(token_file_name, scopes)

        if not creds or creds and not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file_path, scopes)
                creds = flow.run_local_server(port=63154)
                with open(token_file_name, 'w') as token_file:
                    token_file.write(creds.to_json())

        return build('drive', 'v3', credentials=creds)


    def get_all_directories(self):
        """https://developers.google.com/drive/api/v3/reference/files/list
        """
        service = self.init_service(['https://www.googleapis.com/auth/drive.metadata.readonly'])
        dirs = []
        page_token = None
        while True:
            query = service.files().list(
                    # https://developers.google.com/drive/api/guides/ref-search-terms
                    q="mimeType = 'application/vnd.google-apps.folder'",
                    pageSize=100,
                    fields='nextPageToken, files(id, name)',
                    corpora='user',
                    pageToken=page_token)
            results = query.execute()
            dirs.extend(results.get('files', []))
            page_token = results.get('nextPageToken')
            if page_token is None:
                return dirs


    def upload_file_to_directory(self, file_path, mime_type, parent_directory_id):
        """https://developers.google.com/drive/api/v3/reference/files/create
        """
        service = self.init_service(['https://www.googleapis.com/auth/drive.file'])
        files_resource = {
            'name': os.path.basename(file_path),
            'parents': [parent_directory_id]
        }
        # https://developers.google.com/drive/api/guides/manage-uploads
        media = MediaFileUpload(file_path, mimetype=mime_type)
        query = service.files().create(body=files_resource, media_body=media, fields='id')
        file = query.execute()
        return file['id']


    def enable_link_sharing(self, file_id, role, sharing_type):
        """https://developers.google.com/drive/api/v3/reference/permissions/create
        """
        service = self.init_service(['https://www.googleapis.com/auth/drive.file'])
        permissions_resource = {
            'role': role,
            'type': sharing_type
        }
        service.permissions().create(body=permissions_resource, fileId=file_id).execute()

