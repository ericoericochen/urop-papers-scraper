import requests
from bs4 import BeautifulSoup
from user_agent import get_headers


def get_lab_pages(url: str):
    lab_result = requests.get(url, headers=get_headers())

    if lab_result.status_code == 200:
        soup = BeautifulSoup(lab_result.text, "html.parser")
        pagination = soup.select(".pagination-info")[0].text
        tokens = pagination.split(" ")
        pages = int(tokens[-1])

        return (pages, get_lab_pages_generator(soup, url, pages))
    else:
        print(f"UNABLE TO GET {url}")


def get_lab_pages_generator(soup, url: str, pages: int):
    for i in range(0, pages, 3):
        offset = i
        link = url + f"?offset={offset}"
        response = requests.get(link)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        papers_links = soup.select(".artifact-title a")

        links: list[str] = ["https://dspace.mit.edu" + a["href"] for a in papers_links]
        yield links
