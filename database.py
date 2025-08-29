import sqlite3
from typing import List
import re


class Data:
    def __init__(self, keywords: str, url: str):
        self.keywords = keywords
        self.url = url


class Database:
    def __init__(self):
        self.link_conn = sqlite3.connect("links.db")
        self.media_conn = sqlite3.connect("media.db")

    def get_keyword_links(self, keyword_lines: List[str]) -> List[Data]:
        res: List[Data] = []
        cursor = self.link_conn.cursor()

        for line in keyword_lines:
            keywords = normalize(line)

            # Select the first keyword found in the db
            for keyword in keywords:
                search_item = f"%{keyword}%"
                cursor.execute(
                    "SELECT url, topic_tags FROM resources WHERE topic_tags LIKE ?", (search_item.lower(),))
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        res.append(Data(line, row[0]))
                    break

        return res

    def get_keyword_images(self, keyword_lines: List[str]) -> List[Data]:
        res: List[Data] = []
        cursor = self.media_conn.cursor()

        for line in keyword_lines:
            keywords = normalize(line)

            # Select the first keyword found in the db
            for keyword in keywords:
                search_item = f"%{keyword}%"
                cursor.execute(
                    "SELECT url, tags FROM images WHERE tags LIKE ?", (search_item.lower(),))
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        res.append(Data(line, row[0]))
                    break

        return res

    def close(self):
        self.link_conn.close()
        self.media_conn.close()


def normalize(text: str) -> List[str]:
    return re.split(r"[,\s]+", text)
