from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.change_recovery_question_request import ChangeRecoveryQuestionRequest
from openapi_server.models.set_recovery_credential_request import SetRecoveryCredentialRequest
from openapi_server import util


async def change_password(request: web.Request, user_id, body=None) -> web.Response:
    """Change Password

    Change Password

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def change_recovery_question(request: web.Request, user_id, body=None) -> web.Response:
    """Change Recovery Question

    Change Recovery Question

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeRecoveryQuestionRequest.from_dict(body)
    return web.Response(status=200)


async def forgot_password_one_time_code(request: web.Request, user_id, send_email=None) -> web.Response:
    """Forgot Password (One Time Code)

    Forgot Password (One Time Code)

    :param user_id: 
    :type user_id: str
    :param send_email: 
    :type send_email: str

    """
    return web.Response(status=200)


async def set_recovery_credential(request: web.Request, user_id, body=None) -> web.Response:
    """Set Recovery Credential

    Set Recovery Credential

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetRecoveryCredentialRequest.from_dict(body)
    return web.Response(status=200)
