import pandas as pd
from datetime import datetime

class WARNNoticeScraper:
    sheet_id = "19jmo4Cwj933cmSBKV1t0zZ5O-2H5IpiLIhSH9MF8WF0"
    sheet_name = datetime.now().year

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url)
    df = df[['Company Name', 'WARN Date', 'Total Layoffs', 'Begin Date', 'End Date', 'Reason for Layoffs', 'Occupations Impacted']]

    def __init__(self, recipient_name):
        self.recipient_name = recipient_name

    def get_email_body(self):
        return self.df.to_html(index=False)