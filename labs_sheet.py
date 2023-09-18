import time

import gspread
from tqdm import tqdm

from research_paper import ResearchPaper


def stringify_list(lst: list) -> str:
    return ",".join(lst)


class LabsSheet:
    COLS = 7

    def __init__(self, sheet_id: str, credentials_path: str):
        self.gc = gspread.service_account(filename=credentials_path)
        self.sheet = self.gc.open_by_key(sheet_id)

        # assuming worksheets don't change
        self.worksheets = {
            worksheet.title: worksheet.id for worksheet in self.sheet.worksheets()
        }

    def create_lab_worksheet(self, lab_name: str, papers: int):
        self.sheet.add_worksheet(title=lab_name, rows=papers, cols=self.COLS)

    def set_headers(self):
        headers = [
            "Name",
            "Authors",
            "Abstract",
            "Url",
            "Keywords",
            "Date Issued",
            "Files",
        ]

        for worksheet in tqdm(self.sheet.worksheets()):
            worksheet.update("A1:G1", [headers])
            time.sleep(0.5)

    def insert_research_papers(
        self, lab_name: str, research_papers: list[ResearchPaper]
    ):
        worksheet_id = self.worksheets[lab_name]
        worksheet = self.sheet.get_worksheet_by_id(worksheet_id)

        values = [
            [
                paper.title,
                stringify_list(paper.authors),
                paper.abstract,
                paper.url,
                stringify_list(paper.keywords),
                paper.date_issued,
                stringify_list(paper.files),
            ]
            for paper in research_papers
        ]

        worksheet.append_rows(values)
