import requests
from user_agent import get_proxies, get_headers
import asyncio
import aiohttp
import httpx


async def main():
    proxy = get_proxies()["http"]
    print(proxy)
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(
            "https://dspace.mit.edu/handle/1721.1/3549/recent-submissions?offset=270",
            headers=get_headers(),
            proxy=proxy,
            ssl=False,
        ) as res:
            print(res.status)


async def main2():
    proxy = get_proxies()["http"]
    print(proxy)
    with httpx.Client(proxies=proxy) as client:
        async with client.get(
            "https://dspace.mit.edu/handle/1721.1/3549/recent-submissions?offset=270",
            headers=get_headers(),
        ) as res:
            print(res.status)


if __name__ == "__main__":
    res = requests.get(
        "https://dspace.mit.edu/handle/1721.1/3549/recent-submissions?offset=270",
        proxies=get_proxies(),
    )

    print(res.status_code)

    asyncio.run(main2())
    asyncio.run(main())
