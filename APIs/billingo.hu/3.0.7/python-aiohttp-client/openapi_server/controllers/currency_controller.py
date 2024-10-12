from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.conversation_rate import ConversationRate
from openapi_server.models.currency import Currency
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def get_conversion_rate(request: web.Request, _from, to) -> web.Response:
    """Get currencies exchange rate.

    Return with the exchange value of given currencies.

    :param _from: 
    :type _from: dict | bytes
    :param to: 
    :type to: dict | bytes

    """
    _from = .from_dict(_from)
    to = .from_dict(to)
    return web.Response(status=200)
