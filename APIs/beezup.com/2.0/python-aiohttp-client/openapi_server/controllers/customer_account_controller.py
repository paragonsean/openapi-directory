from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_info import AccountInfo
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_email_request import ChangeEmailRequest
from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.company_info import CompanyInfo
from openapi_server.models.credit_card_info import CreditCardInfo
from openapi_server.models.credit_card_info_response import CreditCardInfoResponse
from openapi_server.models.personal_info import PersonalInfo
from openapi_server.models.profile_picture_info import ProfilePictureInfo
from openapi_server.models.profile_picture_info_response import ProfilePictureInfoResponse
from openapi_server import util


async def activate_user_account(request: web.Request, body) -> web.Response:
    """Activate the user account

    

    :param body: The email activation id received by email.
    :type body: str

    """
    return web.Response(status=200)


async def change_email(request: web.Request, body) -> web.Response:
    """Change user email

    

    :param body: 
    :type body: dict | bytes

    """
    body = ChangeEmailRequest.from_dict(body)
    return web.Response(status=200)


async def change_password(request: web.Request, body) -> web.Response:
    """Change user password

    

    :param body: 
    :type body: dict | bytes

    """
    body = ChangePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def get_credit_card_info(request: web.Request, if_none_match=None) -> web.Response:
    """Get credit card information

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_profile_picture_info(request: web.Request, if_none_match=None) -> web.Response:
    """Get profile picture information

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_user_account_info(request: web.Request, if_none_match=None) -> web.Response:
    """Get user account information

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def resend_email_activation(request: web.Request, ) -> web.Response:
    """Resend email activation

    


    """
    return web.Response(status=200)


async def save_company_info(request: web.Request, body) -> web.Response:
    """Change company information

    

    :param body: 
    :type body: dict | bytes

    """
    body = CompanyInfo.from_dict(body)
    return web.Response(status=200)


async def save_credit_card_info(request: web.Request, body) -> web.Response:
    """Save user credit card info

    

    :param body: Credit card info
    :type body: dict | bytes

    """
    body = CreditCardInfo.from_dict(body)
    return web.Response(status=200)


async def save_personal_info(request: web.Request, body) -> web.Response:
    """Save user personal information

    

    :param body: 
    :type body: dict | bytes

    """
    body = PersonalInfo.from_dict(body)
    return web.Response(status=200)


async def save_profile_picture_info(request: web.Request, body) -> web.Response:
    """Change user picture information

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProfilePictureInfo.from_dict(body)
    return web.Response(status=200)
