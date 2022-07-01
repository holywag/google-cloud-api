from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload
from google_oauth import GoogleOAuth

class ValueRenderOption:
    """https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption
    """
    FORMATTED_VALUE = 'FORMATTED_VALUE'
    UNFORMATTED_VALUE = 'UNFORMATTED_VALUE'
    FORMULA = 'FORMULA'

class ValueInputOption:
    """https://developers.google.com/sheets/api/reference/rest/v4/ValueInputOption
    """
    INPUT_VALUE_OPTION_UNSPECIFIED = 'INPUT_VALUE_OPTION_UNSPECIFIED'
    RAW = 'RAW'
    USER_ENTERED = 'USER_ENTERED'

class GoogleSheetsApi:
    """Wrapper for 'sheets' service of Google Cloud API.
    Google Sheets functionality:
        - 
    """


    def __init__(self, credentials):
        self.service = build('sheets', 'v4', credentials=credentials)

    
    def get_range(self, spreadsheet_id, range_, value_render_option):
        """https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get
        """
        request = self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=range_, valueRenderOption=value_render_option)
        # https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#ValueRange
        value_range = request.execute()
        return value_range['values']


    def update_range(self, spreadsheet_id, range_, array_of_rows, value_input_option, include_values_in_response=False, response_value_render_option=ValueRenderOption.FORMATTED_VALUE):
        """https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/update
        """
        value_range = {
            'range': range_,
            'majorDimension': 'ROWS',   # https://developers.google.com/sheets/api/reference/rest/v4/Dimension
            'values': array_of_rows
        }
        request = self.service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_, body=value_range,
            valueInputOption=value_input_option,
            includeValuesInResponse=include_values_in_response,
            responseValueRenderOption=response_value_render_option)
        # https://developers.google.com/sheets/api/reference/rest/v4/UpdateValuesResponse
        update_values_response = request.execute()
        return update_values_response['updatedData']['values'] if include_values_in_response else None

