__author__ = 'Milad'
import tornado.httpserver
import tornado
from tornado.options import options, define
import tornado.web
import tornado.ioloop
from urls import url_pattern
import os
# from ui_modules import main_module

define("port", default=8585, help="run on the given port", type=int)


class WebSystemApplication(tornado.web.Application):
    def __init__(self):
        handlers = url_pattern
        settings = dict(
            debug=True,
            autoreload=True,
            cookie_secret="61oETz3455%545g%#21F%C",
            template_path=os.path.join(os.path.dirname(__file__), "template"),
            static_path=os.path.join(os.path.dirname(__file__), "static/assets"),
            **{
                'pycket': {
                    'engine': 'redis',
                    'storage': {
                        'host': '127.0.0.1',
                        'port': 6379,
                        'db_sessions': 10,
                        'db_notifications': 11,
                        'max_connections': 2 ** 31,
                    },
                    'cookies': {
                        'expires_days': 100,
                    },
                },
            }
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(WebSystemApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
