from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def beta_scrape_product_copy(request: web.Request, url=None) -> web.Response:
    """[BETA] Scrape Product Copy

    To update a product, please use the listed attributes listed underneath. 

    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def products(request: web.Request, =None) -> web.Response:
    """Products

    This resource lists all products that are currently saved in you account.

    :param : 
    :type : str

    """
    return web.Response(status=200)


async def products1(request: web.Request, =None) -> web.Response:
    """Products

    Products

    :param : 
    :type : str

    """
    return web.Response(status=200)
