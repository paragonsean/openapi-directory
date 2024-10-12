from typing import List, Dict
from aiohttp import web

from openapi_server.models.automatic_transition_info_list import AutomaticTransitionInfoList
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.configure_automatic_transition_request import ConfigureAutomaticTransitionRequest
from openapi_server import util


async def configure_automatic_transitions(request: web.Request, body) -> web.Response:
    """Configure new or existing automatic Order status transition

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConfigureAutomaticTransitionRequest.from_dict(body)
    return web.Response(status=200)


async def get_automatic_transitions(request: web.Request, store_id=None, if_none_match=None) -> web.Response:
    """Get list of configured automatic Order status transitions

    

    :param store_id: The StoreId to filter by
    :type store_id: str
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)
