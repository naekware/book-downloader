import requests
import re
from bs4 import BeautifulSoup
from dataclasses import dataclass
from argparse import ArgumentParser


@dataclass
class LibGenBook:
    def __init__(self, author: str, title: str, book_format: str, mirror: str):
        self.author = author
        self.title = title
        self.book_format = book_format
        self.mirror = mirror

    def __str__(self):
        return f"{self.author} / {self.title} / {self.book_format} / {self.mirror}"

    def get_direct_download(self) -> str:
        page = requests.get(self.mirror)
        soup = BeautifulSoup(page.content, "html.parser")

        a_tags = soup.find_all("a")

        for a_tag in a_tags:
            a_tag = str(a_tag)
            if "GET" in a_tag:
                return a_tag.split('"')[1]

        return "download"


class LibGenParser:
    def __init__(self, search_query: str, num: int = 10):
        self.search_query = search_query
        self.num = num
        self.libgen_url = f"https://libgen.is/search.php?req={self.search_query}&open=0&res={self.num}&view=simple&phrase=1&column=def"

    def parse_row_cells(self, cells: list[str]) -> LibGenBook | None:
        if len(cells) < 11:
            return None

        author = (
            ""
            if not (author_match := re.search(r"\>([\w\s\d]+)\<", str(cells[1])))
            else author_match.group(1)
        )
        book = (
            ""
            if not (book_match := re.search(r"\>([\w\s\d]+)\<", str(cells[2])))
            else book_match.group(1)
        )
        book_format = (
            ""
            if not (book_format_match := re.search(r"\>([\w\s\d]+)\<", str(cells[8])))
            else book_format_match.group(1)
        )
        mirror = (
            ""
            if not (mirror_match := re.search(r"href=\"(.+)\"\s", str(cells[9])))
            else mirror_match.group(1)
        )

        if book == "Title":
            return None

        return LibGenBook(author, book, book_format, mirror)

    def parse_books(self):
        page = requests.get(self.libgen_url)
        soup = BeautifulSoup(page.content, "html.parser")
        table_rows = soup.find_all("tr")
        print("= == naek libgen parser == = ")
        for table_row in table_rows:
            cells = table_row.find_all("td")
            book = self.parse_row_cells(cells)
            if book:
                print("====================")
                print(f"Book: {book}")
                print(f"Download: {book.get_direct_download()}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--query", "-q")
    parser.add_argument("--num", "-n")
    args = parser.parse_args()
    LibGenParser(f"{args.query}").parse_books()
