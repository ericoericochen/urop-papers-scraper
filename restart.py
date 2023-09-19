import asyncio
from labs import get_labs
from labs_sheet import LabsSheet
from tqdm import tqdm
from research_paper import ResearchPaper
from lab_pages import get_lab_pages, get_num_lab_pages
import time
import math


def papers_from_urls(urls: list[str]):
    return [ResearchPaper.from_url(url) for url in urls]


async def apapers_from_urls(urls: list[str]):
    papers = [ResearchPaper.afrom_url(url) for url in urls]
    papers = await asyncio.gather(*papers)
    papers = [paper for paper in papers if paper is not None]

    return papers


async def sync_scrape_labs(sheet_id: str, start: str):
    print("<START>")
    labs = get_labs()
    labs_sheet = LabsSheet(sheet_id, "./credentials.json")

    lab_names = list(labs.keys())
    lab_index = lab_names.index(start)
    lab_names = lab_names[lab_index:]

    print("<LOOPING>")

    for lab in lab_names:
        lab_url = labs[lab]
        pages = get_num_lab_pages(lab_url)
        print(pages)
        for batch in tqdm(
            get_lab_pages(lab_url, pages), total=math.ceil(pages / 3), desc=lab
        ):
            # papers = await apapers_from_urls(batch)
            papers = papers_from_urls(batch)
            # print(papers)
            labs_sheet.insert_research_papers(lab, papers)
            # time.sleep(1)

        # throttle
        time.sleep(30)

    print("<DONE!>")


if __name__ == "__main__":
    test_sheet_id = "1lcGJT0_swNAX9XzWQtK_BExrRjK_kuBnn2kuWALSgvY"
    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    # start = "MIT Libraries"
    # start = "MIT Open Access Articles"
    # start = "Sloan School of Management"
    start = ""

    _id = test_sheet_id
    asyncio.run(sync_scrape_labs(_id, start))
