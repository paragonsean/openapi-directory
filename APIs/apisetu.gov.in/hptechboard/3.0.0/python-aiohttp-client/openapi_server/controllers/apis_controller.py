from typing import List, Dict
from aiohttp import web

from openapi_server.models.dipcr400_response import Dipcr400Response
from openapi_server.models.dipcr401_response import Dipcr401Response
from openapi_server.models.dipcr404_response import Dipcr404Response
from openapi_server.models.dipcr500_response import Dipcr500Response
from openapi_server.models.dipcr502_response import Dipcr502Response
from openapi_server.models.dipcr503_response import Dipcr503Response
from openapi_server.models.dipcr504_response import Dipcr504Response
from openapi_server.models.dipcr_request import DipcrRequest
from openapi_server import util


async def dipcr(request: web.Request, body=None) -> web.Response:
    """Diploma Certificate

    API to verify Diploma Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DipcrRequest.from_dict(body)
    return web.Response(status=200)
