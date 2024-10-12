from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_gift_list200_response import GetGiftList200Response
from openapi_server import util


async def get_gift_list(request: web.Request, content_type, accept, list_id) -> web.Response:
    """Get Gift List

    Retrieves information about a Gift List by its ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param list_id: Gift List unique numerical identifier.
    :type list_id: int

    """
    return web.Response(status=200)
