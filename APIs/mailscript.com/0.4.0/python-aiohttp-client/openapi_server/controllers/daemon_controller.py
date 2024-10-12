from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_daemon_token200_response import GetDaemonToken200Response
from openapi_server import util


async def get_daemon_token(request: web.Request, daemon) -> web.Response:
    """Get a token for opening a daemon connection

    

    :param daemon: name of Daemon
    :type daemon: str

    """
    return web.Response(status=200)
