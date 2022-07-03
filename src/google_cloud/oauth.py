import os.path
from hashlib import sha256
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class GoogleOAuthScopes:
    DRIVE_FILE = 'https://www.googleapis.com/auth/drive.file'
    DRIVE_METADATA_READONLY = 'https://www.googleapis.com/auth/drive.metadata.readonly'
    SHEETS = 'https://www.googleapis.com/auth/spreadsheets'
    SHEETS_READONLY = 'https://www.googleapis.com/auth/spreadsheets.readonly'

class GoogleOAuth:
    """Provide Google Cloud authentication capabilities using oauth.
    """


    def __init__(self, credentials_file_path):
        self.credentials_file_path = credentials_file_path


    def authenticate(self, *scopes):
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

        return creds
