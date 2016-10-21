__author__ = 'Milad'

import tornado.web
import requests
import json


class News_Handler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        data = requests.get("http://www.servicefarsi.com/api/news/5530839454796/4/item=0,page=1")
        state = requests.get("http://www.servicefarsi.com/api/news/5530839454796/4/item=19,type=0,page=1")
        data = json.loads(data.text)
        state = json.loads(state.text)

        if not data['err']:
            data_res = data['res']
            list_ = []
            for s in range(0, 5):
                for item in data_res:
                    list_.append(item)
        data_ = state['res']

        self.render("index.html", data_res=data_res, list_ = list_,data_ = data_)
        pass

    def post(self, *args, **kwargs):
        pass
