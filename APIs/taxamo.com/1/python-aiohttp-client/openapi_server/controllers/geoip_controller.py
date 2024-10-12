from typing import List, Dict
from aiohttp import web

from openapi_server.models.locate_given_ip_out import LocateGivenIPOut
from openapi_server.models.locate_my_ip_out import LocateMyIPOut
from openapi_server import util


async def locate_given_ip(request: web.Request, ip) -> web.Response:
    """Locate provided IP

    

    :param ip: IP address.
    :type ip: str

    """
    return web.Response(status=200)


async def locate_my_ip(request: web.Request, ) -> web.Response:
    """Locate IP

    


    """
    return web.Response(status=200)
