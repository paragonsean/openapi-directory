from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def uuid_get(request: web.Request, count=None) -> web.Response:
    """uuid_get

    Generate a random UUID (v4).

    :param count: Number of UUID&#39;s to generate (defaults to 1)
    :type count: int

    """
    return web.Response(status=200)


async def uuid_version_version_get(request: web.Request, version, count=None, type=None, text=None) -> web.Response:
    """uuid_version_version_get

    Generate a random UUID (v4).

    :param version: Version of the UUID spec to use. (0-5), Use &#39;0&#39; for nil (00000000-0000-0000-0000-000000000000) UUID.
    :type version: int
    :param count: Number of UUID&#39;s to generate (defaults to 1)
    :type count: int
    :param type: For v3 and v5 of UUID Spec you can supply the type (dns/url/oid/x500/nil).
    :type type: str
    :param text: For v3 and v5 of UUID Spec supply the text value for the type specified dns/url/oid/x500/nil. For example specify a dns/domain string if the type is \&quot;dns\&quot;
    :type text: str

    """
    return web.Response(status=200)
