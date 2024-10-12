from typing import List, Dict
from aiohttp import web

from openapi_server.models.ndcer400_response import Ndcer400Response
from openapi_server.models.ndcer401_response import Ndcer401Response
from openapi_server.models.ndcer404_response import Ndcer404Response
from openapi_server.models.ndcer500_response import Ndcer500Response
from openapi_server.models.ndcer502_response import Ndcer502Response
from openapi_server.models.ndcer503_response import Ndcer503Response
from openapi_server.models.ndcer504_response import Ndcer504Response
from openapi_server.models.ndcer_request import NdcerRequest
from openapi_server import util


async def ndcer(request: web.Request, body=None) -> web.Response:
    """No Dues/ Objection Certificate

    API to verify No Dues/ Objection Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = NdcerRequest.from_dict(body)
    return web.Response(status=200)
