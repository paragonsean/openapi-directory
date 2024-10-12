from typing import List, Dict
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.cncer400_response import Cncer400Response
from openapi_server.models.cncer401_response import Cncer401Response
from openapi_server.models.cncer404_response import Cncer404Response
from openapi_server.models.cncer500_response import Cncer500Response
from openapi_server.models.cncer502_response import Cncer502Response
from openapi_server.models.cncer503_response import Cncer503Response
from openapi_server.models.cncer504_response import Cncer504Response
from openapi_server.models.cncer_request import CncerRequest
from openapi_server.models.mutan_request import MutanRequest
from openapi_server import util


async def cncer(request: web.Request, body=None) -> web.Response:
    """Conversion Certificate

    API to verify Conversion Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CncerRequest.from_dict(body)
    return web.Response(status=200)


async def mutan(request: web.Request, body=None) -> web.Response:
    """Mutation Report/ePattadar Passbook

    API to verify Mutation Report/ePattadar Passbook.

    :param body: Request format
    :type body: dict | bytes

    """
    body = MutanRequest.from_dict(body)
    return web.Response(status=200)
