from typing import List, Dict
from aiohttp import web

from openapi_server.models.adcrd400_response import Adcrd400Response
from openapi_server.models.adcrd401_response import Adcrd401Response
from openapi_server.models.adcrd404_response import Adcrd404Response
from openapi_server.models.adcrd500_response import Adcrd500Response
from openapi_server.models.adcrd502_response import Adcrd502Response
from openapi_server.models.adcrd503_response import Adcrd503Response
from openapi_server.models.adcrd504_response import Adcrd504Response
from openapi_server.models.adcrd_request import AdcrdRequest
from openapi_server import util


async def adcrd(request: web.Request, body=None) -> web.Response:
    """Admit Card

    API to verify Admit Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AdcrdRequest.from_dict(body)
    return web.Response(status=200)
