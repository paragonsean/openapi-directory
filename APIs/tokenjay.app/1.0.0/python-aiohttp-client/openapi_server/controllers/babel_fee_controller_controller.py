from typing import List, Dict
from aiohttp import web

from openapi_server.models.ergo_pay_response import ErgoPayResponse
from openapi_server.models.mosaik_app import MosaikApp
from openapi_server.models.notification_check_response import NotificationCheckResponse
from openapi_server import util


async def check_for_notifications(request: web.Request, ) -> web.Response:
    """check_for_notifications

    


    """
    return web.Response(status=200)


async def ergo_pay_create_babel_box1(request: web.Request, box_id) -> web.Response:
    """ergo_pay_create_babel_box1

    

    :param box_id: 
    :type box_id: str

    """
    return web.Response(status=200)


async def get_babel_fee_overview(request: web.Request, ) -> web.Response:
    """get_babel_fee_overview

    


    """
    return web.Response(status=200)
