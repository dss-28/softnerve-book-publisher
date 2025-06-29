from playwright.sync_api import sync_playwright
import os

def scrape_chapter(url, output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=f"{output_folder}/screenshot.png", full_page=True)

        content = page.inner_text("#mw-content-text")
        with open(f"{output_folder}/chapter.txt", "w", encoding="utf-8") as f:
            f.write(content)

        browser.close()

if __name__ == "__main__":
    scrape_chapter("https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1")

