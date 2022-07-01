#!/usr/bin/env python3

import argparse
from google_drive import GoogleDriveApi
from google_oauth import GoogleOAuthScopes, GoogleOAuth

parser = argparse.ArgumentParser()
parser.add_argument('file_path')
parser.add_argument('mime_type')
parser.add_argument('parent_directory_id')
args = parser.parse_args()

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.DRIVE_FILE)
drive = GoogleDriveApi(creds)

print(f'Uploading {args.file_path}')

file_id = drive.upload_file_to_directory(args.file_path, args.mime_type, args.parent_directory_id)

print('Enabling link sharing')

drive.enable_link_sharing(file_id, "reader", "anyone")
