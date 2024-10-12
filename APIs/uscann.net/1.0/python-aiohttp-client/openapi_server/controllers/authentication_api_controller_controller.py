from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_model import EmailModel
from openapi_server.models.forgot_mail_token import ForgotMailToken
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.login_user import LoginUser
from openapi_server.models.mail_token import MailToken
from openapi_server.models.problem import Problem
from openapi_server.models.registration_model import RegistrationModel
from openapi_server.models.response_status import ResponseStatus
from openapi_server import util


async def authenticate_user(request: web.Request, content_type, login_user) -> web.Response:
    """authenticate the user and returns the token

    

    :param content_type: 
    :type content_type: str
    :param login_user: The LoginUser definition used to returns the token for authentication
    :type login_user: dict | bytes

    """
    login_user = LoginUser.from_dict(login_user)
    return web.Response(status=200)


async def forgot_password(request: web.Request, content_type, forgot_password) -> web.Response:
    """forgotPassword

    

    :param content_type: 
    :type content_type: str
    :param forgot_password: The User email used to send email
    :type forgot_password: dict | bytes

    """
    forgot_password = EmailModel.from_dict(forgot_password)
    return web.Response(status=200)


async def register(request: web.Request, content_type, register) -> web.Response:
    """register

    

    :param content_type: 
    :type content_type: str
    :param register: The RegistrationForm definition is used to register the customer
    :type register: dict | bytes

    """
    register = RegistrationModel.from_dict(register)
    return web.Response(status=200)


async def set_forgot_password(request: web.Request, content_type, token) -> web.Response:
    """validates the mail token and set new password

    

    :param content_type: 
    :type content_type: str
    :param token: The ForgotMailToken definition used to returns status of password reset
    :type token: dict | bytes

    """
    token = ForgotMailToken.from_dict(token)
    return web.Response(status=200)


async def validate_mail_token(request: web.Request, content_type, token) -> web.Response:
    """validates the mail token

    

    :param content_type: 
    :type content_type: str
    :param token: The MailToken definition used to returns status of validation
    :type token: dict | bytes

    """
    token = MailToken.from_dict(token)
    return web.Response(status=200)
