#!/usr/bin/env python3

from google_drive import GoogleDriveApi

print('Listing all directories:')

for item in GoogleDriveApi('credentials.json').get_all_directories():
    print(item)
