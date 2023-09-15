import asyncio

from lab_pages import get_lab_pages
from lab import Lab

if __name__ == "__main__":
    url = "https://dspace.mit.edu/handle/1721.1/39126?show=full"

    # asyncio.run(Lab.afrom_url(url))
    pages, links_generator = get_lab_pages(
        "https://dspace.mit.edu/handle/1721.1/39118/recent-submissions"
    )

    print(pages)

    for links in links_generator:
        print(links)
