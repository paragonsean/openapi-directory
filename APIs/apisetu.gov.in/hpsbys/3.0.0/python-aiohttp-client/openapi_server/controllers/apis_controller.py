from typing import List, Dict
from aiohttp import web

from openapi_server.models.rsbyc400_response import Rsbyc400Response
from openapi_server.models.rsbyc401_response import Rsbyc401Response
from openapi_server.models.rsbyc404_response import Rsbyc404Response
from openapi_server.models.rsbyc500_response import Rsbyc500Response
from openapi_server.models.rsbyc502_response import Rsbyc502Response
from openapi_server.models.rsbyc503_response import Rsbyc503Response
from openapi_server.models.rsbyc504_response import Rsbyc504Response
from openapi_server.models.rsbyc_request import RsbycRequest
from openapi_server import util


async def rsbyc(request: web.Request, body=None) -> web.Response:
    """Health Card/ Certificate

    API to verify Health Card/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RsbycRequest.from_dict(body)
    return web.Response(status=200)
