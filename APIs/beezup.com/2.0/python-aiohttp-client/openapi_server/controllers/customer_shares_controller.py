from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.error_response_message_payment_required import ErrorResponseMessagePaymentRequired
from openapi_server.models.store_shares import StoreShares
from openapi_server import util


async def delete_store_share(request: web.Request, store_id, user_id) -> web.Response:
    """Delete a share of a store to another user

    

    :param store_id: Your store identifier
    :type store_id: str
    :param user_id: The friend user id
    :type user_id: str

    """
    return web.Response(status=200)


async def get_store_shares(request: web.Request, store_id, if_none_match=None) -> web.Response:
    """Get shares related to this store

    

    :param store_id: Your store identifier
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def share_store(request: web.Request, store_id, body) -> web.Response:
    """Share a store to another user

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: Your friend&#39;s email
    :type body: str

    """
    return web.Response(status=200)
