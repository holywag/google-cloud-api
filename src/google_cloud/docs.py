from googleapiclient.discovery import build

class ReplaceAllTextRequest:
    """https://developers.google.com/docs/api/reference/rest/v1/documents/request#replacealltextrequest
    """
    def __init__(self, contains_text, replace_text, match_case=True):
        self.request = {
            'replaceAllText': { 
                'containsText': {
                    'text': contains_text,
                    'matchCase': 'true' if match_case else 'false'
                }, 
                'replaceText': replace_text
            }}

class GoogleDocsApi:
    def __init__(self, credentials):
        self.service = build('docs', 'v1', credentials=credentials)

    def batch_update(self, document_id, requests):
        """https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate
        """
        result = self.service.documents().batchUpdate(
            documentId=document_id,
            body={'requests': [r.request for r in requests]}).execute()
        return result['replies']

