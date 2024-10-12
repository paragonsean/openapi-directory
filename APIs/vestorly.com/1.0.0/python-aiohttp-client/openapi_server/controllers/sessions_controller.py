from typing import List, Dict
from aiohttp import web

from openapi_server.models.session import Session
from openapi_server.models.session_logout_response import SessionLogoutResponse
from openapi_server import util


async def login(request: web.Request, username, password) -> web.Response:
    """login

    Login To Vestorly Platform

    :param username: Username in the vestorly platform
    :type username: str
    :param password: Password in Vestorly Platform
    :type password: str

    """
    return web.Response(status=200)


async def logout(request: web.Request, vestorly_auth, id) -> web.Response:
    """logout

    Logout of the vestorly platform

    :param vestorly_auth: Authenication token
    :type vestorly_auth: str
    :param id: ID of pet to session
    :type id: str

    """
    return web.Response(status=200)
