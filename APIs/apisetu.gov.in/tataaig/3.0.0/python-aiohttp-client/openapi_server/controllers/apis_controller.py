from typing import List, Dict
from aiohttp import web

from openapi_server.models.podoc400_response import Podoc400Response
from openapi_server.models.podoc401_response import Podoc401Response
from openapi_server.models.podoc404_response import Podoc404Response
from openapi_server.models.podoc500_response import Podoc500Response
from openapi_server.models.podoc502_response import Podoc502Response
from openapi_server.models.podoc503_response import Podoc503Response
from openapi_server.models.podoc504_response import Podoc504Response
from openapi_server.models.podoc_request import PodocRequest
from openapi_server import util


async def podoc(request: web.Request, body=None) -> web.Response:
    """Policy Document

    API to verify Policy Document.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PodocRequest.from_dict(body)
    return web.Response(status=200)
