from typing import List, Dict
from aiohttp import web

from openapi_server.models.cvcer400_response import Cvcer400Response
from openapi_server.models.cvcer401_response import Cvcer401Response
from openapi_server.models.cvcer404_response import Cvcer404Response
from openapi_server.models.cvcer500_response import Cvcer500Response
from openapi_server.models.cvcer502_response import Cvcer502Response
from openapi_server.models.cvcer503_response import Cvcer503Response
from openapi_server.models.cvcer504_response import Cvcer504Response
from openapi_server.models.cvcer_request import CvcerRequest
from openapi_server import util


async def cvcer(request: web.Request, body=None) -> web.Response:
    """Caste Validity Certificate

    API to verify Caste Validity Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CvcerRequest.from_dict(body)
    return web.Response(status=200)
