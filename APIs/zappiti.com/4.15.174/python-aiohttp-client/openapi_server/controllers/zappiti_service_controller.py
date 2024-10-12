from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_zappiti_service_request import CheckZappitiServiceRequest
from openapi_server.models.check_zappiti_service_result import CheckZappitiServiceResult
from openapi_server.models.install_zappiti_service_request import InstallZappitiServiceRequest
from openapi_server.models.install_zappiti_service_result import InstallZappitiServiceResult
from openapi_server.models.start_zappiti_service_request import StartZappitiServiceRequest
from openapi_server.models.start_zappiti_service_result import StartZappitiServiceResult
from openapi_server import util


async def check_zappiti_service_post(request: web.Request, body) -> web.Response:
    """Check if Zappiti Service app status on the player

    ErrorCode.NotInstalled ErrorCode.NotRunning ErrorCode.Running 

    :param body: 
    :type body: dict | bytes

    """
    body = CheckZappitiServiceRequest.from_dict(body)
    return web.Response(status=200)


async def install_zappiti_service_post(request: web.Request, body) -> web.Response:
    """Open a popup that allow the user to install Zappiti Service, if not already installed

    

    :param body: 
    :type body: dict | bytes

    """
    body = InstallZappitiServiceRequest.from_dict(body)
    return web.Response(status=200)


async def start_zappiti_service_post(request: web.Request, body) -> web.Response:
    """Start Zappiti Service if not started yet

    

    :param body: 
    :type body: dict | bytes

    """
    body = StartZappitiServiceRequest.from_dict(body)
    return web.Response(status=200)
