import sqlite3

class Database:
    def __init__(self):
        self.link_conn = sqlite3.connect("links.db")
        self.media_conn = sqlite3.connect("media.db")

    def get_keyword_links(self):
        pass

    def get_keyword_images(self):
        pass
    
    def close(self):
        self.link_conn.close()
        self.media_conn.close()