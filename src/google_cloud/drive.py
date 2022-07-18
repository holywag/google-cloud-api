import os.path
from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload

class GoogleDriveApi:
    """Wrapper for 'drive' service of Google Cloud API.
    Google Drive functionality:
        - list all directories
        - upload a file to a given directory
        - set file permissions
    """


    def __init__(self, credentials):
        self.service = build('drive', 'v3', credentials=credentials)


    def list_directories(self):
        """https://developers.google.com/drive/api/v3/reference/files/list
        """
        dirs = []
        page_token = None
        while True:
            query = self.service.files().list(
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

    
    def find_first_file(self, file_name, parent_directory_id=None, mime_type=None, include_trashed=False):
        """https://developers.google.com/drive/api/v3/reference/files/list
        """
        # https://developers.google.com/drive/api/guides/ref-search-terms
        query_string = f"name = '{file_name}' and trashed = {'true' if include_trashed else 'false'}"
        if parent_directory_id is not None:
            query_string = query_string + f" and '{parent_directory_id}' in parents"
        if mime_type is not None:
            query_string = query_string + f" and mimeType = '{mime_type}'"
        query = self.service.files().list(
            q=query_string,
            pageSize=1,
            fields='files(id)',
            corpora='user')
        # https://developers.google.com/drive/api/v3/reference/files#resource-representations
        files = query.execute().get('files', [])
        return files[0]['id'] if len(files) else None


    def get_file_permissions(self, file_id):
        """https://developers.google.com/drive/api/v3/reference/files/get
        """
        query = self.service.files().get(
            fileId=file_id,
            fields='permissions(role, type, emailAddress)')
        # https://developers.google.com/drive/api/v3/reference/permissions#resource-representations
        return query.execute().get('permissions', [])


    def upload_file_to_directory(self, file_path, mime_type, parent_directory_id):
        """https://developers.google.com/drive/api/v3/reference/files/create
        """
        files_resource = {
            'name': os.path.basename(file_path),
            'parents': [parent_directory_id]
        }
        # https://developers.google.com/drive/api/guides/manage-uploads
        media = MediaFileUpload(file_path, mimetype=mime_type)
        query = self.service.files().create(body=files_resource, media_body=media, fields='id')
        file = query.execute()
        return file['id']


    def enable_link_sharing(self, file_id, role, sharing_type):
        """https://developers.google.com/drive/api/v3/reference/permissions/create
        """
        permissions_resource = {
            'role': role,
            'type': sharing_type
        }
        self.service.permissions().create(body=permissions_resource, fileId=file_id).execute()

