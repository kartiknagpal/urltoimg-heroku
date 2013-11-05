#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from dependencies import web
from capture import urltoimg

#import xml.etree.ElementTree as ET

# tree = ET.parse('acess_key.xml')
# root = tree.getroot()

urls = (
    '/urltoimg', 'get_screenshot'
)

app = web.application(urls, globals())

class get_screenshot:
    def GET(self):
        get_params = web.input()
        urltoimg(get_params['url'])
        web.header("Content-Type", "images/png") # Set the Header
        return open('capture.png',"rb").read() # Notice 'rb' for reading images

if __name__ == '__main__':
    app.run()
    