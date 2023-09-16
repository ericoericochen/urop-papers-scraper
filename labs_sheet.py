import gspread


class LabsSheet:
    COLS = 7

    def __init__(self, sheet_id: str, credentials_path: str):
        self.gc = gspread.service_account(filename=credentials_path)
        self.sheet = self.gc.open_by_key(sheet_id)

    def create_lab_worksheet(self, lab_name: str, papers: int):
        self.sheet.add_worksheet(title=lab_name, rows=papers, cols=self.COLS)
