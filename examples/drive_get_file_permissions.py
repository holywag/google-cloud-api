#!/usr/bin/env python3

import argparse
from google_cloud.drive import GoogleDriveApi
from google_cloud.oauth import GoogleOAuthScopes, GoogleOAuth

parser = argparse.ArgumentParser()
parser.add_argument('file_id')
args = parser.parse_args()

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.DRIVE_METADATA_READONLY)
drive = GoogleDriveApi(creds)
print(drive.get_file_permissions(args.file_id))
