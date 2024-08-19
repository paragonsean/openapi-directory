from typing import List, Dict
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.fetch_action_response import FetchActionResponse
from openapi_server.models.mosaik_app import MosaikApp
from openapi_server import util


async def do_create_babel_box(request: web.Request, body) -> web.Response:
    """do_create_babel_box

    

    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)


async def ergo_pay_create_babel_box(request: web.Request, address, token_id, erg_amount, token_amount) -> web.Response:
    """ergo_pay_create_babel_box

    

    :param address: 
    :type address: str
    :param token_id: 
    :type token_id: str
    :param erg_amount: 
    :type erg_amount: int
    :param token_amount: 
    :type token_amount: int

    """
    return web.Response(status=200)


async def get_babel_fee_new_offer(request: web.Request, ) -> web.Response:
    """get_babel_fee_new_offer

    


    """
    return web.Response(status=200)


async def replace_token_amount_input_fields(request: web.Request, body) -> web.Response:
    """replace_token_amount_input_fields

    

    :param body: 
    :type body: Dict[str, ]

    """
    return web.Response(status=200)
