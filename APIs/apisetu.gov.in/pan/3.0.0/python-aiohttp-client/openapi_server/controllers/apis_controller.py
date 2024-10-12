from typing import List, Dict
from aiohttp import web

from openapi_server.models.pan_verification_record_schema import PANVerificationRecordSchema
from openapi_server.models.pancr400_response import Pancr400Response
from openapi_server.models.pancr401_response import Pancr401Response
from openapi_server.models.pancr404_response import Pancr404Response
from openapi_server.models.pancr500_response import Pancr500Response
from openapi_server.models.pancr502_response import Pancr502Response
from openapi_server.models.pancr503_response import Pancr503Response
from openapi_server.models.pancr504_response import Pancr504Response
from openapi_server.models.pancr_request import PancrRequest
from openapi_server import util


async def pancr(request: web.Request, body=None) -> web.Response:
    """PAN Verification Record

    API to verify PAN Verification Record.

    :param body: Request format
    :type body: dict | bytes

    """
    body = PancrRequest.from_dict(body)
    return web.Response(status=200)
