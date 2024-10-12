from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.quick_connect_result import QuickConnectResult
from openapi_server.models.quick_connect_state import QuickConnectState
from openapi_server import util


async def activate(request: web.Request, ) -> web.Response:
    """Temporarily activates quick connect for five minutes.

    


    """
    return web.Response(status=200)


async def authorize(request: web.Request, code) -> web.Response:
    """Authorizes a pending quick connect request.

    

    :param code: Quick connect code to authorize.
    :type code: str

    """
    return web.Response(status=200)


async def available(request: web.Request, status=None) -> web.Response:
    """Enables or disables quick connect.

    

    :param status: New MediaBrowser.Model.QuickConnect.QuickConnectState.
    :type status: dict | bytes

    """
    status = .from_dict(status)
    return web.Response(status=200)


async def connect(request: web.Request, secret) -> web.Response:
    """Attempts to retrieve authentication information.

    

    :param secret: Secret previously returned from the Initiate endpoint.
    :type secret: str

    """
    return web.Response(status=200)


async def deauthorize(request: web.Request, ) -> web.Response:
    """Deauthorize all quick connect devices for the current user.

    


    """
    return web.Response(status=200)


async def get_status(request: web.Request, ) -> web.Response:
    """Gets the current quick connect state.

    


    """
    return web.Response(status=200)


async def initiate(request: web.Request, ) -> web.Response:
    """Initiate a new quick connect request.

    


    """
    return web.Response(status=200)
