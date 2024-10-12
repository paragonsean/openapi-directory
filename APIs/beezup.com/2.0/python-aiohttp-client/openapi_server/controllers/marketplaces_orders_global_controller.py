from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_synchronization_list import AccountSynchronizationList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.order_index import OrderIndex
from openapi_server import util


async def get_marketplace_accounts_synchronization(request: web.Request, store_id=None, if_none_match=None) -> web.Response:
    """[DEPRECATED] Get current synchronization status between your marketplaces and BeezUP accounts

    Use /orders/v3

    :param store_id: The StoreId to filter by
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_order_index(request: web.Request, if_none_match=None) -> web.Response:
    """[DEPRECATED] Get all actions you can do on the order API

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def harvest_all(request: web.Request, store_id=None) -> web.Response:
    """[DEPRECATED] Send harvest request to all your marketplaces

    

    :param store_id: The StoreId to filter by
    :type store_id: str

    """
    return web.Response(status=200)
