from typing import List, Dict
from aiohttp import web

from openapi_server.models.reset_password_model import ResetPasswordModel
from openapi_server.models.set_password_model import SetPasswordModel
from openapi_server import util


async def password_has_user_set_password(request: web.Request, ) -> web.Response:
    """Determines if the currently logged in user has set their own password

    


    """
    return web.Response(status=200)


async def password_password_requirements(request: web.Request, ) -> web.Response:
    """Gets the password complexity requirements

    


    """
    return web.Response(status=200)


async def password_reset_by_model(request: web.Request, model) -> web.Response:
    """Resets the password for the supplied user name

    

    :param model: 
    :type model: dict | bytes

    """
    model = ResetPasswordModel.from_dict(model)
    return web.Response(status=200)


async def password_set_by_model(request: web.Request, model) -> web.Response:
    """Sets the password for the currently logged in user

    

    :param model: 
    :type model: dict | bytes

    """
    model = SetPasswordModel.from_dict(model)
    return web.Response(status=200)
