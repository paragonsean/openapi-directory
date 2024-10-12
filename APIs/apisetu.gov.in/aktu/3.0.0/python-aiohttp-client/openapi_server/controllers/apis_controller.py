from typing import List, Dict
from aiohttp import web

from openapi_server.models.dgcer400_response import Dgcer400Response
from openapi_server.models.dgcer401_response import Dgcer401Response
from openapi_server.models.dgcer404_response import Dgcer404Response
from openapi_server.models.dgcer500_response import Dgcer500Response
from openapi_server.models.dgcer502_response import Dgcer502Response
from openapi_server.models.dgcer503_response import Dgcer503Response
from openapi_server.models.dgcer504_response import Dgcer504Response
from openapi_server.models.dgcer_request import DgcerRequest
from openapi_server.models.dgmst_request import DgmstRequest
from openapi_server import util


async def dgcer(request: web.Request, body=None) -> web.Response:
    """Degree/ Diploma Certificate

    API to verify Degree/ Diploma Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DgcerRequest.from_dict(body)
    return web.Response(status=200)


async def dgmst(request: web.Request, body=None) -> web.Response:
    """Degree/ Diploma Marksheet

    API to verify Degree/ Diploma Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DgmstRequest.from_dict(body)
    return web.Response(status=200)
