import aiohttp
import requests
from bs4 import BeautifulSoup

from user_agent import get_headers


class ResearchPaper:
    def __init__(self, html: str):
        soup = BeautifulSoup(html, "html.parser")

        # extract table rows
        rows = self.get_rows(soup)

        # get title
        title = soup.select(".page-header.first-page-header")[0].text

        # get authors
        authors = self.extract_properties(rows, "dc.contributor.author")

        # get abstract
        abstracts = self.extract_properties(rows, "dc.description.abstract")
        abstract = "\n".join(abstracts)

        # get date issued
        date_issued = self.extract_properties(rows, "dc.date.issued")
        date_issued = date_issued[0] if len(date_issued) > 0 else ""

        # get keywords
        keywords = []
        keyword_terms = self.extract_properties(rows, "dc.subject")

        for term in keyword_terms:
            split = term.split(",")
            for keyword in split:
                keywords.append(keyword.strip())

        # get url
        url = self.extract_properties(rows, "dc.identifier.uri")[0]

        # get files
        files_rows = soup.select(".file-list .file-wrapper.row")
        files = []

        for file_row in files_rows:
            link = "https://dspace.mit.edu" + file_row.find("a")["href"]
            files.append(link)

        # set up properties
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.date_issued = date_issued
        self.keywords = keywords
        self.url = url
        self.files = files

    def extract_properties(self, rows, property: str) -> list[str]:
        properties = [row["value"] for row in rows if row["name"] == property]

        return properties

    def get_rows(self, soup: BeautifulSoup):
        metadata = soup.find("table")
        table_rows = metadata.select(".ds-table-row")

        rows = []

        for table_row in table_rows:
            name = table_row.find("td", attrs={"class": "label-cell"}).text
            value = table_row.find("td", attrs={"class": "word-break"}).text

            rows.append({"name": name, "value": value})

        return rows

    @staticmethod
    def from_url(url: str):
        html = requests.get(url).text

        return ResearchPaper(html)

    @staticmethod
    async def afrom_url(url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=get_headers()) as res:
                html = await res.text()

                return ResearchPaper(html)
