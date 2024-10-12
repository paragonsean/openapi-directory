from typing import List, Dict
from aiohttp import web

from openapi_server.models.govid400_response import Govid400Response
from openapi_server.models.govid401_response import Govid401Response
from openapi_server.models.govid404_response import Govid404Response
from openapi_server.models.govid500_response import Govid500Response
from openapi_server.models.govid502_response import Govid502Response
from openapi_server.models.govid503_response import Govid503Response
from openapi_server.models.govid504_response import Govid504Response
from openapi_server.models.govid_request import GovidRequest
from openapi_server import util


async def govid(request: web.Request, body=None) -> web.Response:
    """ID Card

    API to verify ID Card.

    :param body: Request format
    :type body: dict | bytes

    """
    body = GovidRequest.from_dict(body)
    return web.Response(status=200)


async def phcer(request: web.Request, body=None) -> web.Response:
    """Pharmacist Registration Certificate

    API to verify Pharmacist Registration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = GovidRequest.from_dict(body)
    return web.Response(status=200)
