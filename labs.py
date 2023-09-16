import requests
from bs4 import BeautifulSoup, NavigableString
from urllib.parse import urlparse


def get_labs():
    labs_url = "https://dspace.mit.edu/community-list"
    res = requests.get(labs_url)
    soup = BeautifulSoup(res.text, "html.parser")
    labs_list = soup.select(
        "#aspect_artifactbrowser_CommunityBrowser_referenceSet_community-browser"
    )[0]
    lab_rows = [child for child in labs_list.children]

    labs = []

    for lab in lab_rows:
        if isinstance(lab, NavigableString):
            continue

        class_name = lab.get("class", [])

        if "hidden" in class_name:
            continue

        labs.append(lab)

    lab_links = [
        lab.find("a", attrs={"name": "community-browser-link"}) for lab in labs
    ]

    labs_dict = {}

    parsed_url = urlparse(labs_url)
    domain = parsed_url.scheme + "://" + parsed_url.netloc

    for lab in lab_links:
        lab_name = lab.text
        href = lab.get("href")
        link = domain + href + "/recent-submissions"
        labs_dict[lab_name] = link

    return labs_dict
