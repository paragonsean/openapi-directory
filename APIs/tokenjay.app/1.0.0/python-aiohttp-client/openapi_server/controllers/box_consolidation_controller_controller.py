from typing import List, Dict
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.mosaik_app import MosaikApp
from openapi_server import util


async def ep_consolidate(request: web.Request, p2pkaddress) -> web.Response:
    """ep_consolidate

    

    :param p2pkaddress: 
    :type p2pkaddress: str

    """
    return web.Response(status=200)


async def main_app1(request: web.Request, ) -> web.Response:
    """main_app1

    


    """
    return web.Response(status=200)
