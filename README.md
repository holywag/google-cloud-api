# Google Cloud Platform APIs

```
pip install -r requirements.txt
```

## Googel Drive: list all directories

```
python drive_list_all_directories.py
```

## Googel Drive: upload a file and set up link sharing

```
python drive_upload_and_share.py 5XKX-5PP6-PMC0-9C08.pdf application/pdf 1Mx9GkYlDJ1_46BCl8rwseIIAR50bIoPk
```

## Googel Sheets: get range of values from a given sheet

```
python sheets_get_range.py 1QqBhEd8qtvWD9t1QNDVD30zJe_Jeskp4e1VbGymDD_k 'Electric!H4'
```

## Google Sheets: update a range of values in a given sheet

```
python sheets_update_range.py 1QqBhEd8qtvWD9t1QNDVD30zJe_Jeskp4e1VbGymDD_k 'Electric!H10' '=HYPERLINK("google.com", "Google Search")'
```
