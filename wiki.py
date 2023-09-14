# Digikala Web Scarping Using PlayWright Asynco
# digikala.com

from bs4 import BeautifulSoup
import asyncio
import re
from playwright.async_api import async_playwright



async def get_html():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        url = "https://fa.wikipedia.org/wiki/%D8%A7%DB%8C%D8%B1%D8%A7%D9%86"
        await page.goto(url)
        await page.wait_for_selector('h3')
        return await page.content()


def read_content(html):
    soup = BeautifulSoup(html, "html.parser")
    texts = soup.find_all("p")
    for text in texts:
        clean_text = re.sub(r'\[\d+\]',"",text.text)
        print(clean_text,end="")



global links
links = []
counter = 0
html = asyncio.run(get_html())
read_content(html)
