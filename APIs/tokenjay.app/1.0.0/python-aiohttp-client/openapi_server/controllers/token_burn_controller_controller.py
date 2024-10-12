from typing import List, Dict
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.mosaik_app import MosaikApp
from openapi_server import util


async def get_burning_transaction(request: web.Request, uuid) -> web.Response:
    """get_burning_transaction

    

    :param uuid: 
    :type uuid: str

    """
    return web.Response(status=200)


async def main_app(request: web.Request, ) -> web.Response:
    """main_app

    


    """
    return web.Response(status=200)


async def prepare_transaction(request: web.Request, body) -> web.Response:
    """prepare_transaction

    

    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)
