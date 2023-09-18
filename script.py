import asyncio
from labs import get_labs
from labs_sheet import LabsSheet
from tqdm import tqdm
from research_paper import ResearchPaper
from lab_pages import get_lab_pages, get_num_lab_pages
import time
import math


async def scrape_labs():
    print("<START>")
    labs = get_labs()

    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    labs_sheet = LabsSheet(sheet_id, "./credentials.json")

    tasks = [scrape_lab(lab, labs[lab], labs_sheet) for lab in labs]

    await asyncio.gather(*tasks)
    print("<DONE!>")


def papers_from_urls(urls: list[str]):
    return [ResearchPaper.from_url(url) for url in urls]


async def apapers_from_urls(urls: list[str]):
    papers = [ResearchPaper.afrom_url(url) for url in urls]

    return await asyncio.gather(*papers)


async def scrape_lab(lab: str, lab_url: str, labs_sheet: LabsSheet):
    pages = get_num_lab_pages(lab_url)
    for batch in tqdm(
        get_lab_pages(lab_url, pages), total=math.ceil(pages / 3), desc=lab
    ):
        papers = await apapers_from_urls(batch)

        labs_sheet.insert_research_papers(lab, papers)

        time.sleep(2)  # prevent being rate limited


async def sync_scrape_labs():
    print("<START>")
    labs = get_labs()

    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    labs_sheet = LabsSheet(sheet_id, "./credentials.json")

    for lab in labs:
        lab_url = labs[lab]
        pages = get_num_lab_pages(lab_url)
        for batch in tqdm(
            get_lab_pages(lab_url, pages), total=math.ceil(pages / 3), desc=lab
        ):
            papers = await apapers_from_urls(batch)
            labs_sheet.insert_research_papers(lab, papers)
            time.sleep(1)

        break

    print("<DONE!>")


if __name__ == "__main__":
    asyncio.run(sync_scrape_labs())
