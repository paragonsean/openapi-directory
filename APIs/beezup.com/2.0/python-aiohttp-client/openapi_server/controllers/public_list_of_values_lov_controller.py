from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.public_list_of_values_response import PublicListOfValuesResponse
from openapi_server.models.public_lov_index import PublicLovIndex
from openapi_server import util


async def get_public_list_of_values(request: web.Request, list_name, accept_language=None, if_none_match=None) -> web.Response:
    """Get the list of values related to this list name

    

    :param list_name: The list of value name your want to get
    :type list_name: str
    :param accept_language: Indicates that the client accepts the following languages.
    :type accept_language: List[str]
    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_public_lov_index(request: web.Request, if_none_match=None) -> web.Response:
    """Get all list names

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)
