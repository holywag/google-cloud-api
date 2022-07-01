#!/usr/bin/env python3

import argparse
from google_sheets import GoogleSheetsApi, ValueRenderOption
from google_oauth import GoogleOAuthScopes, GoogleOAuth

parser = argparse.ArgumentParser()
parser.add_argument('spreadsheet_id')
parser.add_argument('range')
args = parser.parse_args()

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.SHEETS_READONLY)
sheets = GoogleSheetsApi(creds)

print(sheets.get_range(args.spreadsheet_id, args.range, ValueRenderOption.FORMULA))
