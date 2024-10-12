from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.login_user import LoginUser
from openapi_server.models.problem import Problem
from openapi_server.models.response_status import ResponseStatus
from openapi_server import util


async def authenticate_user(request: web.Request, login_user) -> web.Response:
    """Get Token

    

    :param login_user: The LoginUser definition used to returns the token for authentication
    :type login_user: dict | bytes

    """
    login_user = LoginUser.from_dict(login_user)
    return web.Response(status=200)


async def register(request: web.Request, register) -> web.Response:
    """Customer Registration

    

    :param register: The RegistrationForm definition is used to register the customer
    :type register: dict | bytes

    """
    register = Customer.from_dict(register)
    return web.Response(status=200)
