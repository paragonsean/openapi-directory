from typing import List, Dict
from aiohttp import web

from openapi_server.models.nncer400_response import Nncer400Response
from openapi_server.models.nncer401_response import Nncer401Response
from openapi_server.models.nncer404_response import Nncer404Response
from openapi_server.models.nncer500_response import Nncer500Response
from openapi_server.models.nncer502_response import Nncer502Response
from openapi_server.models.nncer503_response import Nncer503Response
from openapi_server.models.nncer504_response import Nncer504Response
from openapi_server.models.nncer_request import NncerRequest
from openapi_server import util


async def nncer(request: web.Request, body=None) -> web.Response:
    """Non-Encumbrance Certificate

    API to verify Non-Encumbrance Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = NncerRequest.from_dict(body)
    return web.Response(status=200)
