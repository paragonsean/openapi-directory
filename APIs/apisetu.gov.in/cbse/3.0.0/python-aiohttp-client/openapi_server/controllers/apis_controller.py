from typing import List, Dict
from aiohttp import web

from openapi_server.models.academic_certificate_schema import AcademicCertificateSchema
from openapi_server.models.hpcer400_response import Hpcer400Response
from openapi_server.models.hpcer401_response import Hpcer401Response
from openapi_server.models.hpcer404_response import Hpcer404Response
from openapi_server.models.hpcer500_response import Hpcer500Response
from openapi_server.models.hpcer502_response import Hpcer502Response
from openapi_server.models.hpcer503_response import Hpcer503Response
from openapi_server.models.hpcer504_response import Hpcer504Response
from openapi_server.models.hpcer_request import HpcerRequest
from openapi_server.models.hscer_request import HscerRequest
from openapi_server.models.tetcr_request import TetcrRequest
from openapi_server import util


async def hpcer(request: web.Request, body=None) -> web.Response:
    """Class XII Passing Certificate

    API to verify Class XII Passing Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def hscer(request: web.Request, body=None) -> web.Response:
    """Class XII Marksheet

    API to verify Class XII Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HscerRequest.from_dict(body)
    return web.Response(status=200)


async def hsmgr(request: web.Request, body=None) -> web.Response:
    """Class XII Migration Certificate

    API to verify Class XII Migration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def nchsc(request: web.Request, body=None) -> web.Response:
    """NCHMCT Skill Certificate (X)

    API to verify NCHMCT Skill Certificate (X).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def nctsc(request: web.Request, body=None) -> web.Response:
    """NCHMCT Skill Certificate (XII)

    API to verify NCHMCT Skill Certificate (XII).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def nsesc(request: web.Request, body=None) -> web.Response:
    """NSE Skill Certificate (X)

    API to verify NSE Skill Certificate (X).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def nstsc(request: web.Request, body=None) -> web.Response:
    """NSE Skill Certificate (XII)

    API to verify NSE Skill Certificate (XII).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def ntltr(request: web.Request, body=None) -> web.Response:
    """NEET Rank Letter

    API to verify NEET Rank Letter.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def ntmks(request: web.Request, body=None) -> web.Response:
    """NEET Marksheet

    API to verify NEET Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def skhsc(request: web.Request, body=None) -> web.Response:
    """Skill Certificate (X)

    API to verify Skill Certificate (X).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def sktsc(request: web.Request, body=None) -> web.Response:
    """Skill Certificate (XII)

    API to verify Skill Certificate (XII).

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def spcer(request: web.Request, body=None) -> web.Response:
    """Class X Passing Certificate

    API to verify Class X Passing Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def sscer(request: web.Request, body=None) -> web.Response:
    """Class X Marksheet

    API to verify Class X Marksheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HscerRequest.from_dict(body)
    return web.Response(status=200)


async def ssmgr(request: web.Request, body=None) -> web.Response:
    """Class X Migration Certificate

    API to verify Class X Migration Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = HpcerRequest.from_dict(body)
    return web.Response(status=200)


async def tetcr(request: web.Request, body=None) -> web.Response:
    """Teachers Eligibility Test Certificate

    API to verify Teachers Eligibility Test Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TetcrRequest.from_dict(body)
    return web.Response(status=200)


async def tetms(request: web.Request, body=None) -> web.Response:
    """Teachers Eligibility Test Mark Sheet

    API to verify Teachers Eligibility Test Mark Sheet.

    :param body: Request format
    :type body: dict | bytes

    """
    body = TetcrRequest.from_dict(body)
    return web.Response(status=200)
