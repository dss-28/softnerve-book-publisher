from scraper import scrape_chapter
from agents import ai_writer, ai_reviewer
from feedback_loop import human_feedback_loop
from store_and_search import store_final_text

if __name__ == "__main__":
    url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scrape_chapter(url)

    with open("output/chapter.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    written = ai_writer(raw)
    reviewed = ai_reviewer(written)

    with open("output/final_draft.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)

    human_feedback_loop()
    store_final_text()