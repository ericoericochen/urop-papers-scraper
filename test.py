from lab import Lab
import asyncio

if __name__ == "__main__":
    url = "https://dspace.mit.edu/handle/1721.1/39126?show=full"

    asyncio.run(Lab.afrom_url(url))
