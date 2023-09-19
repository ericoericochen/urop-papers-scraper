import requests
from bs4 import BeautifulSoup
from user_agent import get_headers, get_proxies
import urllib.parse
from retrying import retry


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


WAIT = 10 * 60 * 1000


@retry(wait_exponential_multiplier=60 * 1000, wait_exponential_max=WAIT)
def get_num_lab_pages(url: str):
    lab_result = requests.get(url, headers=get_headers(), proxies=get_proxies())

    if lab_result.status_code == 200:
        soup = BeautifulSoup(lab_result.text, "html.parser")
        pagination = soup.select(".pagination-info")[0].text
        tokens = pagination.split(" ")
        pages = int(tokens[-1])

        return pages
    else:
        print(lab_result.status_code)
        print(f"UNABLE TO GET {url}")
        print(lab_result.headers)
        print("RETRYING in the next 3 minutes")
        raise RuntimeError


@retry(wait_exponential_multiplier=60 * 1000, wait_exponential_max=WAIT)
def get_paper_links(link: str):
    response = requests.get(link, headers=get_headers(), proxies=get_proxies())

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        papers_links = soup.select(".artifact-title a")

        links: list[str] = [
            add_query_param("https://dspace.mit.edu" + a["href"], "show", "full")
            for a in papers_links
        ]

        return links
    else:
        print(response.status_code)
        print(f"UNABLE TO GET {link}")
        print(response.headers)
        print("RETRYING in the next 3 minutes")
        raise RuntimeError


def get_lab_pages(url: str, pages: int):
    for i in range(0, pages, 3):
        offset = i
        link = url + f"?offset={offset}"

        links = get_paper_links(link)

        yield links
