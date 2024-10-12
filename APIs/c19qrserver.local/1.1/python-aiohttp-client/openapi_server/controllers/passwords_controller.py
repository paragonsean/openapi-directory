from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_token import InvalidToken
from openapi_server.models.request_password_reset_response import RequestPasswordResetResponse
from openapi_server.models.sample import Sample
from openapi_server.models.sample2 import Sample2
from openapi_server.models.sample4 import Sample4
from openapi_server import util


async def change_password_post(request: web.Request, body) -> web.Response:
    """Used for changing your password

    Pass in your old password and your new password

    :param body: Change Password Payload
    :type body: dict | bytes

    """
    body = Sample.from_dict(body)
    return web.Response(status=200)


async def request_password_reset_post(request: web.Request, body) -> web.Response:
    """Used for requesting a password reset code

    The admin should run this on behalf of a user who forgot their password.  The API will generate a password reset code which the admin should then provide to the user. The user can use their client to reset their password. Normally the password reset code is mailed to the user, but I didn&#39;t want to do this in this case because I didn&#39;t want to  introduce the complicated dependency of having an SMTP server just for this purpose. Doing it this way makes it easy for people to adopt this  API. 

    :param body: Request Password Reset Payload
    :type body: dict | bytes

    """
    body = Sample2.from_dict(body)
    return web.Response(status=200)


async def verify_password_change_post(request: web.Request, body) -> web.Response:
    """Used for resetting your password when you forgot it

    Another endpoint will generate a password reset code for you. You should  use the client app to submit the reset code along with the new password to change your password. 

    :param body: Password Reset Payload
    :type body: dict | bytes

    """
    body = Sample4.from_dict(body)
    return web.Response(status=200)
