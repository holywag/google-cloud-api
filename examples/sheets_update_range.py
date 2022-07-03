#!/usr/bin/env python3

import argparse
from google_cloud.sheets import GoogleSheetsApi, ValueRenderOption, ValueInputOption
from google_cloud.oauth import GoogleOAuthScopes, GoogleOAuth

parser = argparse.ArgumentParser()
parser.add_argument('spreadsheet_id')
parser.add_argument('range')
parser.add_argument('values', nargs='+')
args = parser.parse_args()

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.SHEETS)
sheets = GoogleSheetsApi(creds)

print(sheets.update_range(
    args.spreadsheet_id,
    args.range,
    [args.values],
    ValueInputOption.USER_ENTERED,
    True,
    ValueRenderOption.FORMATTED_VALUE))
