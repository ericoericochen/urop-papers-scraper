from labs_sheet import LabsSheet

if __name__ == "__main__":
    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    labs_sheet = LabsSheet(sheet_id, "./credentials.json")

    labs_sheet.set_headers()
