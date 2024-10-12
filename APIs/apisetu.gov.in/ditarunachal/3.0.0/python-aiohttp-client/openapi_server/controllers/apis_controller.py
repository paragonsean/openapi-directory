from typing import List, Dict
from aiohttp import web

from openapi_server.models.ilpmt400_response import Ilpmt400Response
from openapi_server.models.ilpmt401_response import Ilpmt401Response
from openapi_server.models.ilpmt404_response import Ilpmt404Response
from openapi_server.models.ilpmt500_response import Ilpmt500Response
from openapi_server.models.ilpmt502_response import Ilpmt502Response
from openapi_server.models.ilpmt503_response import Ilpmt503Response
from openapi_server.models.ilpmt504_response import Ilpmt504Response
from openapi_server.models.ilpmt_request import IlpmtRequest
from openapi_server import util


async def ilpmt(request: web.Request, body=None) -> web.Response:
    """Inner Line Permit

    API to verify Inner Line Permit.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IlpmtRequest.from_dict(body)
    return web.Response(status=200)
