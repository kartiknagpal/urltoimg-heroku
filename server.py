#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from dependencies import web
from capture import urltoimg
import base64

#import xml.etree.ElementTree as ET
# tree = ET.parse('acess_key.xml')
# root = tree.getroot()

urls = (
	'/', 'index',
    '/urltoimg', 'get_screenshot'
)

app = web.application(urls, globals())
render = web.template.render('templates/')
my_form = web.form.Form(web.form.Textbox('', class_='textfield', id='url'),)

class get_screenshot:
    def GET(self):
		get_params = web.input()
		filename = urltoimg(get_params['url'])
		print filename
		web.header("Content-Type", "images/png")
		if 'attachment' in get_params and get_params['attachment'].lower() == 'true':
			web.header('Content-Disposition', 'attachment; filename='+filename)
			return open('static'+'/'+filename,"rb").read()
		elif 'base64' in get_params and get_params['base64'].lower() == 'true':
		    getFile = file( 'static'+'/'+filename, 'rb' )
		    web.header('Content-type','application/octet-stream')
		    web.header('Content-transfer-encoding','base64') 
		    base64data = base64.standard_b64encode(getFile.read())
		    return base64data
		raise web.seeother('static'+'/'+filename)

class index:
	def GET(self):
		form = my_form()
		return render.index(form, "Url To Image Web Service.")

if __name__ == '__main__':
    app.run()
    