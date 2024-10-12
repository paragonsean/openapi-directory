from typing import List, Dict
from aiohttp import web

from openapi_server.models.login_model import LoginModel
from openapi_server.models.public_session_info_model import PublicSessionInfoModel
from openapi_server import util


async def auth_login_by_model(request: web.Request, model) -> web.Response:
    """Start a session with the DomainProviders user store

    

    :param model: DomainProvider username and password
    :type model: dict | bytes

    """
    model = LoginModel.from_dict(model)
    return web.Response(status=200)


async def auth_logout(request: web.Request, ) -> web.Response:
    """auth_logout

    


    """
    return web.Response(status=200)


async def auth_password_requirements(request: web.Request, ) -> web.Response:
    """Gets the login rules

    


    """
    return web.Response(status=200)


async def auth_resume_session(request: web.Request, ) -> web.Response:
    """Validate and extend the duration of a session

    


    """
    return web.Response(status=200)
