import aiohttp
import requests
from bs4 import BeautifulSoup
import time

from user_agent import get_headers, get_proxies


class ResearchPaper:
    def __init__(self, html: str):
        soup = BeautifulSoup(html, "html.parser")

        # extract table rows
        rows = self.get_rows(soup)

        # get title
        title = self.extract_properties(rows, "dc.title")

        if len(title) > 0:
            title = title[0]
        else:
            title = ""

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
        url = self.extract_properties(rows, "dc.identifier.uri")

        if len(url) > 0:
            url = url[0]
        else:
            url = ""

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
        try:
            metadata = soup.find("table")
            table_rows = metadata.select(".ds-table-row")

            rows = []

            for table_row in table_rows:
                name = table_row.find("td", attrs={"class": "label-cell"}).text
                value = table_row.find("td", attrs={"class": "word-break"}).text

                rows.append({"name": name, "value": value})

            return rows
        except:
            # print(soup.prettify())

            return []

    @staticmethod
    def from_url(url: str):
        try:
            req = requests.get(url, headers=get_headers(), proxies=get_proxies())

            if req.status_code != 200:
                print(req.status_code)
                raise RuntimeError

            html = req.text

            return ResearchPaper(html)
        except:
            print(f"Failed to get {url}")
            with open("log.txt", "w") as file:
                file.write(f"{url}\n")

    @staticmethod
    async def afrom_url(url: str):
        for attempts in range(3):
            try:
                async with aiohttp.ClientSession(headers=get_headers()) as session:
                    async with session.get(url) as res:
                        if res.status == 200:
                            try:
                                html = await res.text()
                                return ResearchPaper(html)
                            except:
                                return None
                        else:
                            print(res.status)
                            print(f"UNABLE TO GET {url}")
                            print(res.headers)
                            print(
                                f"RETRYING in the next {(attempts + 1) * 5 * 60} seconds"
                            )
                            raise RuntimeError
            except:
                time.sleep((attempts + 1) * 5 * 60)

        print(f"Failed to get {url}")

        # record failed paper
        with open("log.txt", "w") as file:
            file.write(f"{url}\n")

        return None
