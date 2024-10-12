from typing import List, Dict
from aiohttp import web

from openapi_server.models.pvcer400_response import Pvcer400Response
from openapi_server.models.pvcer401_response import Pvcer401Response
from openapi_server.models.pvcer404_response import Pvcer404Response
from openapi_server.models.pvcer500_response import Pvcer500Response
from openapi_server.models.pvcer502_response import Pvcer502Response
from openapi_server.models.pvcer503_response import Pvcer503Response
from openapi_server.models.pvcer504_response import Pvcer504Response
from openapi_server.models.pvcer_request import PvcerRequest
from openapi_server import util


async def pvcer(request: web.Request, body=None) -> web.Response:
    """Provisional Certificate

    API to verify Provisional Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PvcerRequest.from_dict(body)
    return web.Response(status=200)
