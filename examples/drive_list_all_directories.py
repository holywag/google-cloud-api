#!/usr/bin/env python3

from google_cloud.drive import GoogleDriveApi
from google_cloud.oauth import GoogleOAuthScopes, GoogleOAuth

print('Listing all directories:')

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.DRIVE_METADATA_READONLY)
drive = GoogleDriveApi(creds)
for item in drive.list_directories():
    print(item)
