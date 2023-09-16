from labs import get_labs
from labs_sheet import LabsSheet
from lab_pages import get_num_lab_pages
from tqdm import tqdm
import time

if __name__ == "__main__":
    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    creds_path = "credentials.json"

    labs_sheet = LabsSheet(sheet_id=sheet_id, credentials_path=creds_path)
    labs = get_labs()
    lab_names = labs.keys()

    pbar = tqdm(lab_names)
    for lab_name in pbar:
        lab_url = labs[lab_name]
        num_papers = get_num_lab_pages(lab_url)

        pbar.set_postfix(lab=lab_name)
        labs_sheet.create_lab_worksheet(lab_name, papers=num_papers)
        time.sleep(1)
