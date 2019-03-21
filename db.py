import sqlite3

class Db:

    def __init__(self):
        self.conn = sqlite3.connect('shorturl.db')
        self.create_table_if_not_exist()


    def create_table_if_not_exist(self):
        cursor = self.conn.cursor()
        try:
            check_sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='urls';"
            create_sql = "CREATE TABLE urls ( id INTEGER PRIMARY KEY AUTOINCREMENT, url varchar, UNIQUE(url) );"
            init_sql = "insert into urls(id, url) values (12121,'http://www.baidu.com');"
            res = cursor.execute(check_sql).fetchone()
            if not res:
                cursor.execute(create_sql)
                cursor.execute(init_sql)
                self.conn.commit()
        except sqlite3.OperationalError:
            pass
        finally:
            cursor.close()



    def insert(self, _url):
        insert_url = "INSERT OR IGNORE into urls(url) values ('%s')" % (_url)
        cursor = self.conn.cursor()
        try:
            cursor.execute(insert_url)
            self.conn.commit()
            _id = cursor.lastrowid
            if not _id:
                _id = self.fetch_id(_url)
            return _id
        except sqlite3.OperationalError:
            pass
        finally:
            cursor.close()


    def fetch_id(self, _url):
        query_url = "select id from urls where url = '%s' order by id desc" % _url
        cursor = self.conn.cursor()
        try:
            res = cursor.execute(query_url).fetchone()
            if not res:
                return None
            else:
                return res[0]
        except sqlite3.OperationalError:
            pass
        finally:
            cursor.close()


    def fetch_url(self, _id):
        query_url = "select url from urls where id = '%s'" % _id
        cursor = self.conn.cursor()
        try:
            res = cursor.execute(query_url).fetchone()
            if not res:
                return None
            else:
                return res[0]
        except sqlite3.OperationalError:
            pass
        finally:
            cursor.close()


if __name__ == "__main__":
    url = "http://192.168.9.23/qck/qq"
    print(Db().insert(url))
