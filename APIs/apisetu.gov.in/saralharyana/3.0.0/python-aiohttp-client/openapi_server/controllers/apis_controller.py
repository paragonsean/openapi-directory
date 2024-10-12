from typing import List, Dict
from aiohttp import web

from openapi_server.models.nbcer400_response import Nbcer400Response
from openapi_server.models.nbcer401_response import Nbcer401Response
from openapi_server.models.nbcer404_response import Nbcer404Response
from openapi_server.models.nbcer500_response import Nbcer500Response
from openapi_server.models.nbcer502_response import Nbcer502Response
from openapi_server.models.nbcer503_response import Nbcer503Response
from openapi_server.models.nbcer504_response import Nbcer504Response
from openapi_server.models.nbcer_request import NbcerRequest
from openapi_server import util


async def nbcer(request: web.Request, body=None) -> web.Response:
    """NAC/Birth/Death Certificate

    API to verify NAC/Birth/Death Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = NbcerRequest.from_dict(body)
    return web.Response(status=200)
