Python 3.8.0 (v3.8.0:fa919fdf25, Oct 14 2019, 10:23:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import logging; logging.basicConfig(level=logging.INFO)
>>> import asyncio, os, json, time
>>> from datetime import datetime
>>> from aiohttp import web
>>> async def index(request):  # 参考aiohttp的文档
	#要加content_type这个参数，否则会变成下载文件
	return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')

>>> def init():
	app = web.Application()
	app.add_routes([web.get('/',index)])
	logging.info('Server started at http://127.0.0.1:8080')
	web.run_app(app,host='127.0.0.1',port=8080)

	
>>> init()
INFO:root:Server started at http://127.0.0.1:8080
======== Running on http://127.0.0.1:8080 ========
(Press CTRL+C to quit)
