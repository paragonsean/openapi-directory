from typing import List, Dict
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.btcer400_response import Btcer400Response
from openapi_server.models.btcer401_response import Btcer401Response
from openapi_server.models.btcer404_response import Btcer404Response
from openapi_server.models.btcer500_response import Btcer500Response
from openapi_server.models.btcer502_response import Btcer502Response
from openapi_server.models.btcer503_response import Btcer503Response
from openapi_server.models.btcer504_response import Btcer504Response
from openapi_server.models.btcer_request import BtcerRequest
from openapi_server.models.ctcer_request import CtcerRequest
from openapi_server.models.dmcer_request import DmcerRequest
from openapi_server.models.dpicr_request import DpicrRequest
from openapi_server.models.dtcer_request import DtcerRequest
from openapi_server.models.incer_request import IncerRequest
from openapi_server import util


async def btcer(request: web.Request, body=None) -> web.Response:
    """Birth Certificate

    API to verify Birth Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = BtcerRequest.from_dict(body)
    return web.Response(status=200)


async def ctcer(request: web.Request, body=None) -> web.Response:
    """Caste Certificate

    API to verify Caste Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = CtcerRequest.from_dict(body)
    return web.Response(status=200)


async def dmcer(request: web.Request, body=None) -> web.Response:
    """Domicile Certificate

    API to verify Domicile Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DmcerRequest.from_dict(body)
    return web.Response(status=200)


async def dpicr(request: web.Request, body=None) -> web.Response:
    """Disabled Person Identity Card/ Certificate

    API to verify Disabled Person Identity Card/ Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DpicrRequest.from_dict(body)
    return web.Response(status=200)


async def dtcer(request: web.Request, body=None) -> web.Response:
    """Death Certificate

    API to verify Death Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = DtcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = IncerRequest.from_dict(body)
    return web.Response(status=200)
