#!/usr/bin/env python3

from google_sheets import GoogleSheetsApi, ValueRenderOption
from google_oauth import GoogleOAuthScopes, GoogleOAuth

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.SHEETS_READONLY)
sheets = GoogleSheetsApi(creds)

print(sheets.get_range('1QqBhEd8qtvWD9t1QNDVD30zJe_Jeskp4e1VbGymDD_k', 'Electric!H4', ValueRenderOption.FORMULA))
