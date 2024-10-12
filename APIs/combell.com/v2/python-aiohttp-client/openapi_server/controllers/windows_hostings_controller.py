from typing import List, Dict
from aiohttp import web

from openapi_server.models.windows_hosting import WindowsHosting
from openapi_server.models.windows_hosting_detail import WindowsHostingDetail
from openapi_server import util


async def get_windows_hosting(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Windows hosting detail

    

    :param domain_name: The Windows hosting domain name.
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_windows_hostings(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of windows hostings

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)
