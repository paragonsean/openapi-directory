from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_contact_request_body import CheckContactRequestBody
from openapi_server.models.check_contact_response import CheckContactResponse
from openapi_server import util


async def check_contact(request: web.Request, body) -> web.Response:
    """Check-Contact

    

    :param body: 
    :type body: dict | bytes

    """
    body = CheckContactRequestBody.from_dict(body)
    return web.Response(status=200)
