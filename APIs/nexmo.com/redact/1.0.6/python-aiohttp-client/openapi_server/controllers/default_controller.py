from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_invalid_id import ErrorInvalidId
from openapi_server.models.error_throttled import ErrorThrottled
from openapi_server.models.error_unauthorized import ErrorUnauthorized
from openapi_server.models.redact_message403_response import RedactMessage403Response
from openapi_server.models.redact_message422_response import RedactMessage422Response
from openapi_server.models.redact_transaction import RedactTransaction
from openapi_server import util


async def redact_message(request: web.Request, body) -> web.Response:
    """Redact a specific message

    

    :param body: 
    :type body: dict | bytes

    """
    body = RedactTransaction.from_dict(body)
    return web.Response(status=200)
