from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def lookup(request: web.Request, type, number, _json=None) -> web.Response:
    """lookup

    

    :param type: Allowed values are \&quot;cnam\&quot;, \&quot;format\&quot;, \&quot;hlr\&quot; and \&quot;mnp\&quot;.
    :type type: str
    :param number: The phone number to look up.
    :type number: List[str]
    :param _json: Determines whether the response shall be returned in JSON format. Does not work with type \&quot;format\&quot;.
    :type _json: str

    """
    return web.Response(status=200)


async def lookup_cnam(request: web.Request, number) -> web.Response:
    """lookup_cnam

    

    :param number: The phone number to look up.
    :type number: List[str]

    """
    return web.Response(status=200)


async def lookup_format(request: web.Request, number) -> web.Response:
    """lookup_format

    

    :param number: The phone number to look up.
    :type number: List[str]

    """
    return web.Response(status=200)


async def lookup_hlr(request: web.Request, number) -> web.Response:
    """lookup_hlr

    

    :param number: The phone number to look up.
    :type number: List[str]

    """
    return web.Response(status=200)


async def lookup_mnp(request: web.Request, number, _json=None) -> web.Response:
    """lookup_mnp

    

    :param number: The phone number to look up.
    :type number: List[str]
    :param _json: Determines whether the response shall be returned in JSON format.
    :type _json: str

    """
    return web.Response(status=200)
