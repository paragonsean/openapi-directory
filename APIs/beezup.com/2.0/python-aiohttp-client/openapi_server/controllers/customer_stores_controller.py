from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_store_request import CreateStoreRequest
from openapi_server.models.error_response_message_payment_required import ErrorResponseMessagePaymentRequired
from openapi_server.models.links_get_store_link import LinksGetStoreLink
from openapi_server.models.store import Store
from openapi_server.models.store_list import StoreList
from openapi_server.models.update_store_request import UpdateStoreRequest
from openapi_server import util


async def create_store(request: web.Request, body) -> web.Response:
    """Create a new store

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateStoreRequest.from_dict(body)
    return web.Response(status=200)


async def delete_store(request: web.Request, store_id) -> web.Response:
    """Delete a store

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def get_store(request: web.Request, store_id, if_none_match=None) -> web.Response:
    """Get store&#39;s information

    

    :param store_id: Your store identifier
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_stores(request: web.Request, if_none_match=None) -> web.Response:
    """Get store list

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def update_store(request: web.Request, store_id, body) -> web.Response:
    """Update some store&#39;s information.

    Update some store&#39;s information. FYI, you cannot change the country. 

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateStoreRequest.from_dict(body)
    return web.Response(status=200)
