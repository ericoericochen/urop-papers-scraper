import asyncio
from labs import get_labs
from labs_sheet import LabsSheet
from tqdm import tqdm
from research_paper import ResearchPaper
from lab_pages import get_lab_pages, get_num_lab_pages
import time
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)  # For Chrome


def add_query_param(url, param_name, param_value):
    """
    Add a query parameter to a URL.

    Args:
        url (str): The original URL.
        param_name (str): The name of the query parameter to add.
        param_value (str): The value of the query parameter.

    Returns:
        str: The URL with the added query parameter.
    """
    # Parse the original URL
    parsed_url = urllib.parse.urlparse(url)

    # Get the existing query parameters as a dictionary
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Add the new query parameter
    query_params[param_name] = [param_value]

    # Reconstruct the URL with the added query parameter
    new_url = urllib.parse.urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            urllib.parse.urlencode(
                query_params, doseq=True
            ),  # Use doseq=True to handle multiple values for the same parameter
            parsed_url.fragment,
        )
    )

    return new_url


def papers_from_urls(urls: list[str]):
    papers = []

    for url in urls:
        driver.get(url)
        html = driver.page_source
        paper = ResearchPaper(html)
        papers.append(paper)

    return papers


def get_paper_links(link: str):
    driver.get(link)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    papers_links = soup.select(".artifact-title a")

    links: list[str] = [
        add_query_param("https://dspace.mit.edu" + a["href"], "show", "full")
        for a in papers_links
    ]

    return links


def get_lab_pages(url: str, pages: int):
    for i in range(0, pages, 3):
        offset = i
        link = url + f"?offset={offset}"

        links = get_paper_links(link)

        yield links


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

        break

        # throttle
        time.sleep(30)

    print("<DONE!>")


if __name__ == "__main__":
    test_sheet_id = "1lcGJT0_swNAX9XzWQtK_BExrRjK_kuBnn2kuWALSgvY"
    sheet_id = "1_KX1U1ksj1Bzraf-oWbZh8nDHxQxYzZC1lSSuzgt1OA"
    # start = "MIT Libraries"
    start = "MIT Open Access Articles"

    _id = test_sheet_id
    asyncio.run(sync_scrape_labs(_id, start))
