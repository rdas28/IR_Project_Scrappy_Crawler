import scrapy
from pathlib import Path

class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    start_urls = ["https://en.wikipedia.org/wiki/Machine_learning"]

    custom_settings = {
        "DEPTH_LIMIT": 2,
        "CLOSESPIDER_PAGECOUNT": 20
    }

    def parse(self, response):
        folder = Path("data/crawl_html")
        folder.mkdir(parents=True, exist_ok=True)

        doc_id = response.url.split("/")[-1] + ".html"
        path = folder / doc_id
        path.write_bytes(response.body)

        for link in response.css("a::attr(href)").getall():
            if link.startswith("/wiki/") and ":" not in link:
                yield response.follow(link, callback=self.parse)
