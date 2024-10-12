from typing import List, Dict
from aiohttp import web

from openapi_server.models.agcer400_response import Agcer400Response
from openapi_server.models.agcer401_response import Agcer401Response
from openapi_server.models.agcer404_response import Agcer404Response
from openapi_server.models.agcer500_response import Agcer500Response
from openapi_server.models.agcer502_response import Agcer502Response
from openapi_server.models.agcer503_response import Agcer503Response
from openapi_server.models.agcer504_response import Agcer504Response
from openapi_server.models.agcer_request import AgcerRequest
from openapi_server import util


async def agcer(request: web.Request, body=None) -> web.Response:
    """Agriculture/ Agriculturist Certificate

    API to verify Agriculture/ Agriculturist Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def bacer(request: web.Request, body=None) -> web.Response:
    """Backward Area Certificate

    API to verify Backward Area Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def bhcer(request: web.Request, body=None) -> web.Response:
    """Bonafide Certificate

    API to verify Bonafide Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def chcer(request: web.Request, body=None) -> web.Response:
    """Character Certificate

    API to verify Character Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def dccer(request: web.Request, body=None) -> web.Response:
    """Dogra Class Certificate

    API to verify Dogra Class Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def ffcer(request: web.Request, body=None) -> web.Response:
    """Freedom Fighter Certificate

    API to verify Freedom Fighter Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def incer(request: web.Request, body=None) -> web.Response:
    """Income Certificate

    API to verify Income Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def lhcer(request: web.Request, body=None) -> web.Response:
    """Legal Heir Certificate

    API to verify Legal Heir Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def mncer(request: web.Request, body=None) -> web.Response:
    """Minority Certificate

    API to verify Minority Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def obcer(request: web.Request, body=None) -> web.Response:
    """OBC Certificate

    API to verify OBC Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def psprt(request: web.Request, body=None) -> web.Response:
    """Passport/ Passport Verification

    API to verify Passport/ Passport Verification.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def racer(request: web.Request, body=None) -> web.Response:
    """Rural Area Certificate

    API to verify Rural Area Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def rmcer(request: web.Request, body=None) -> web.Response:
    """Marriage Certificate

    API to verify Marriage Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)


async def shcer(request: web.Request, body=None) -> web.Response:
    """SC/ST  Certificate

    API to verify SC/ST  Certificate.

    :param body: Request format
    :type body: dict | bytes

    """
    body = AgcerRequest.from_dict(body)
    return web.Response(status=200)
