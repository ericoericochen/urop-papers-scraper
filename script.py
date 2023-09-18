import asyncio
from labs import get_labs
from labs_sheet import LabsSheet


async def scrape_labs():
    pass


async def scrape_lab(lab: str, lab_url: str, labs_sheet: LabsSheet):
    pass


if __name__ == "__main__":
    labs = get_labs()

    for lab in labs:
        print(lab)
