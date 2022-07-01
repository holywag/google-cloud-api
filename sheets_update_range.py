#!/usr/bin/env python3

from google_sheets import GoogleSheetsApi, ValueRenderOption, ValueInputOption
from google_oauth import GoogleOAuthScopes, GoogleOAuth

creds = GoogleOAuth('credentials.json').authenticate(GoogleOAuthScopes.SHEETS)
sheets = GoogleSheetsApi(creds)

print(sheets.update_range(
    '1QqBhEd8qtvWD9t1QNDVD30zJe_Jeskp4e1VbGymDD_k',
    'Electric!H10',
    [['=HYPERLINK("https://www.google.com", "Google Search")']],
    ValueInputOption.USER_ENTERED,
    True,
    ValueRenderOption.FORMATTED_VALUE))
