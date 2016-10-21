__author__ = 'Milad'

from handlers.news_handler import News_Handler

url_pattern = [
    ("/",News_Handler)
]