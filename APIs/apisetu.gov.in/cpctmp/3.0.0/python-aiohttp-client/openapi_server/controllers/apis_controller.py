from typing import List, Dict
from aiohttp import web

from openapi_server.models.skmst400_response import Skmst400Response
from openapi_server.models.skmst401_response import Skmst401Response
from openapi_server.models.skmst404_response import Skmst404Response
from openapi_server.models.skmst500_response import Skmst500Response
from openapi_server.models.skmst502_response import Skmst502Response
from openapi_server.models.skmst503_response import Skmst503Response
from openapi_server.models.skmst504_response import Skmst504Response
from openapi_server.models.skmst_request import SkmstRequest
from openapi_server import util


async def skmst(request: web.Request, body=None) -> web.Response:
    """Skill Marksheet/ Score Card

    API to verify Skill Marksheet/ Score Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = SkmstRequest.from_dict(body)
    return web.Response(status=200)
