# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import simplejson as json
from db import Db
from hexconvert import HexConvert

CURRENT_DOMAIN = "http://localhost:8988"

class UrlHandler(tornado.web.RequestHandler):
    def get(self, short_url=None):
        if not short_url:
            self.write("Hello, world")
            raise tornado.web.Finish

        _id = HexConvert().convert64_10(short_url)
        if not _id:
            self.write("Hello, Hello, world")
            raise tornado.web.Finish

        url = Db().fetch_url(_id)
        if not url:
            self.write("Hello, Hello, e")
            raise tornado.web.Finish

        self.redirect(url)

    def post(self):
        try:
            data = tornado.escape.json_decode(self.request.body)
        except json.decoder.JSONDecodeError:
            self.write(json.dumps({"code": 0, "result": "参数格式不正确"}, ensure_ascii=False))
            raise tornado.web.Finish
        except:
            self.write(json.dumps({"code": 0, "result": "其它错误"}, ensure_ascii=False))
            raise tornado.web.Finish

        if not data or 'url' not in data:
            self.write(json.dumps({"code": 0, "result": "参数为空"}, ensure_ascii=False))
            raise tornado.web.Finish

        url = data['url']
        if "http://" not in url and "https://" not in url:
            self.write(json.dumps({"code": 0, "result": "url格式不正确"}, ensure_ascii=False))
            raise tornado.web.Finish

        id_ = Db().insert(url)
        short_url = HexConvert.convert10_64(id_)
        self.write(json.dumps({"code": 1, "result": "success", "short_url": CURRENT_DOMAIN+"/u/"+short_url}, ensure_ascii=False))


def make_app():
    return tornado.web.Application([
        (r"/u/([^/]*)", UrlHandler),
        (r"/u", UrlHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8988)
    tornado.ioloop.IOLoop.current().start()
