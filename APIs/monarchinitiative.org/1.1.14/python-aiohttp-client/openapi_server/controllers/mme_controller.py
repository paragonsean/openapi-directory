from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def post_disease_mme(request: web.Request, body) -> web.Response:
    """Match a patient to diseases based on their phenotypes

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def post_fly_mme(request: web.Request, body) -> web.Response:
    """Match a patient to fruit fly genes based on similar phenotypes

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def post_mouse_mme(request: web.Request, body) -> web.Response:
    """Match a patient to mouse genes based on similar phenotypes

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def post_nematode_mme(request: web.Request, body) -> web.Response:
    """Match a patient to nematode genes based on similar phenotypes

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def post_zebrafish_mme(request: web.Request, body) -> web.Response:
    """Match a patient to zebrafish genes based on similar phenotypes

    

    :param body: 
    :type body: 

    """
    return web.Response(status=200)
