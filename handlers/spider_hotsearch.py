# -*- coding: utf-8 -*-

import json
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import tornado.gen
from tornado.concurrent import run_on_executor

from utils import param_md5, USER_AGENT
from consts import HOTSEARCH_WEIBO_URL, RESPONSE_CODE
from handlers.common import CommonHandler

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
logger = logging.getLogger(__name__)


class WeiboHotsearchHandler(CommonHandler):
    '''
    处理微博热搜请求(/v1/spider/hotsearch/weibo)的Handler
    handle_args：校验传入参数
    '''

    def __init__(self, *args, **kwargs):
        super(WeiboHotsearchHandler, self).__init__(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        super(WeiboHotsearchHandler, self).initialize(*args, **kwargs)

    def handle_args(self):
        request_data = json.loads(self.request.body)
        keyword = request_data['keyword']
        platform = request_data['platform']
        date = request_data['date']
        version = request_data['version']
        token = request_data['token']
        re_token = param_md5(keyword + platform + date + version + 'mo')
        if re_token == token:
            return keyword, platform, date
        else:
            raise ValueError(u'不正常访问token')

    @run_on_executor
    def spider_hotsearch_weibo(self, keyword, platform, date):
        try:
            headers = {
                'User-Agent': USER_AGENT
            }
            req = requests.get(HOTSEARCH_WEIBO_URL % date,
                               headers=headers).json()
            hotsearch_list = []
            for i in req:
                hotsearch_detail = {}
                hotsearch_detail['keyword'] = i['keyword']
                hotsearch_detail['url'] = i['url']
                hotsearch_detail['count'] = i['count']
                hotsearch_detail['searchcount'] = i['searchCount']
                hotsearch_detail['rank'] = i['rank']
                hotsearch_list.append(hotsearch_detail)
            list_all_hotsearch_info = {
                'keyword': keyword,
                'platform': platform,
                'date': date,
                'hotsearch_info': hotsearch_list
            }
            return list_all_hotsearch_info
        except:
            return []

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        try:
            keyword, platform, date = self.handle_args()
        except ValueError as e:
            logger.exception(e)
            self.set_status(RESPONSE_CODE.BAD_REQUEST)
            response = e.message
            self.write(response)
            self.finish()
            return

        try:
            result = yield self.spider_hotsearch_weibo(keyword, platform, date)
        except ValueError as e:
            logger.exception(e)
            self.set_status(RESPONSE_CODE.INTERNAL_SERVER_ERROR)
            response = e.message
            self.write(json.dumps(response))
            self.finish()
            return

        self.set_status(RESPONSE_CODE.OK)
        response = result
        self.write(json.dumps(response))
        self.finish()