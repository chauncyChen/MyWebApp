# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:53:18 2016

@author: chauncyChen
"""

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type = 'text/html',charset='UTF-8')
    

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',2000)
    logging.info('server started at http://127.0.0.1:2000...')
    return srv
    
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()