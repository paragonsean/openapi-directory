from typing import List, Dict
from aiohttp import web

from openapi_server.models.ratcr400_response import Ratcr400Response
from openapi_server.models.ratcr401_response import Ratcr401Response
from openapi_server.models.ratcr404_response import Ratcr404Response
from openapi_server.models.ratcr500_response import Ratcr500Response
from openapi_server.models.ratcr502_response import Ratcr502Response
from openapi_server.models.ratcr503_response import Ratcr503Response
from openapi_server.models.ratcr504_response import Ratcr504Response
from openapi_server.models.ratcr_request import RatcrRequest
from openapi_server import util


async def ratcr(request: web.Request, body=None) -> web.Response:
    """Ration Card

    API to verify Ration Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = RatcrRequest.from_dict(body)
    return web.Response(status=200)
