# -*- coding: utf-8 -*-

import logging
from tornado import web, ioloop, autoreload
from tornado.options import options, define

from routes import routes


define('host', default='127.0.0.1', help='the ip listening on', type=str)
define('port', default=8888, help='run on the given port', type=int)
define('log_path', default='./tmp_log', help='log path ', type=str)

logging.basicConfig(filename='%s/tornado.log' % options.log_path, level=logging.INFO)


def make_app():
    return web.Application(routes, debug=False)


def start_server():
    options.parse_command_line()
    app = make_app()
    try:
        app.listen(options.port, address=options.host)
        loop = ioloop.IOLoop.instance()
        # autoreload.start(loop)
        loop.start()
    except KeyboardInterrupt:
        print 'Server terminated by User.'


if __name__ == '__main__':
    start_server()
