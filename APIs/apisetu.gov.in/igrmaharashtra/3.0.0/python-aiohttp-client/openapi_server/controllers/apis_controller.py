from typing import List, Dict
from aiohttp import web

from openapi_server.models.llcer400_response import Llcer400Response
from openapi_server.models.llcer401_response import Llcer401Response
from openapi_server.models.llcer404_response import Llcer404Response
from openapi_server.models.llcer500_response import Llcer500Response
from openapi_server.models.llcer502_response import Llcer502Response
from openapi_server.models.llcer503_response import Llcer503Response
from openapi_server.models.llcer504_response import Llcer504Response
from openapi_server.models.llcer_request import LlcerRequest
from openapi_server import util


async def llcer(request: web.Request, body=None) -> web.Response:
    """Leave and License Certificate

    API to verify Leave and License Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = LlcerRequest.from_dict(body)
    return web.Response(status=200)
