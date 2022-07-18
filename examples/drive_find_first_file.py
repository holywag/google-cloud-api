#!/usr/bin/env python3

import argparse
from google_cloud.drive import GoogleDriveApi
from google_cloud.oauth import GoogleOAuthScopes, GoogleOAuth

parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument('--mime_type')
parser.add_argument('--parent_directory_id')
args = parser.parse_args()

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.DRIVE_METADATA_READONLY)
drive = GoogleDriveApi(creds)
print(drive.find_first_file(
    args.file_name,
    mime_type=args.mime_type,
    parent_directory_id=args.parent_directory_id))
