from typing import List, Dict
from aiohttp import web

from openapi_server.models.chcer400_response import Chcer400Response
from openapi_server.models.chcer401_response import Chcer401Response
from openapi_server.models.chcer404_response import Chcer404Response
from openapi_server.models.chcer500_response import Chcer500Response
from openapi_server.models.chcer502_response import Chcer502Response
from openapi_server.models.chcer503_response import Chcer503Response
from openapi_server.models.chcer504_response import Chcer504Response
from openapi_server.models.chcer_request import ChcerRequest
from openapi_server import util


async def chcer(request: web.Request, body=None) -> web.Response:
    """Character Certificate

    API to verify Character Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def dncer(request: web.Request, body=None) -> web.Response:
    """Distance Certificate

    API to verify Distance Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def dpcer(request: web.Request, body=None) -> web.Response:
    """Dependency Certificate

    API to verify Dependency Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def fslcs(request: web.Request, body=None) -> web.Response:
    """Food Stuff License

    API to verify Food Stuff License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def grred(request: web.Request, body=None) -> web.Response:
    """Grievance Redressal/ Registration

    API to verify Grievance Redressal/ Registration.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def isoal(request: web.Request, body=None) -> web.Response:
    """Issue of Arm Licence

    API to verify Issue of Arm Licence.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def lvcer(request: web.Request, body=None) -> web.Response:
    """Land Valuation/ Holding/ Record Certificate

    API to verify Land Valuation/ Holding/ Record Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def malcs(request: web.Request, body=None) -> web.Response:
    """Manufacturer License

    API to verify Manufacturer License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def mpkby(request: web.Request, body=None) -> web.Response:
    """Small Savings Agent License

    API to verify Small Savings Agent License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def ritin(request: web.Request, body=None) -> web.Response:
    """Right to Information

    API to verify Right to Information.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def rscer(request: web.Request, body=None) -> web.Response:
    """Residence Certificate

    API to verify Residence Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def shcer(request: web.Request, body=None) -> web.Response:
    """SC/ST  Certificate

    API to verify SC/ST  Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def smcer(request: web.Request, body=None) -> web.Response:
    """Surviving Member Certificate

    API to verify Surviving Member Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def sslcs(request: web.Request, body=None) -> web.Response:
    """Standardized Agency Systems (SAS) Agent License

    API to verify Standardized Agency Systems (SAS) Agent License.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)


async def vrwmi(request: web.Request, body=None) -> web.Response:
    """License/ Verification of Weights, Measures and Instruments

    API to verify License/ Verification of Weights, Measures and Instruments.

    :param body: Request format
    :type body: dict | bytes

    """
    body = ChcerRequest.from_dict(body)
    return web.Response(status=200)
