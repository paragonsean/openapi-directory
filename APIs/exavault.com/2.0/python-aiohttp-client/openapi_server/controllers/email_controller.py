from typing import List, Dict
from aiohttp import web

from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.send_referral_email_request_body import SendReferralEmailRequestBody
from openapi_server import util


async def send_referral_email(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Send referral email to a given address

    Invite a friend to sign up for a free trial of ExaVault. Send a [referral](/lp/referafriend/) email to an email address. If the recipient signs up for ExaVault, we&#39;ll apply a credit to your account for the referral. 

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendReferralEmailRequestBody.from_dict(body)
    return web.Response(status=200)


async def send_welcome_email(request: web.Request, ev_api_key, ev_access_token, username) -> web.Response:
    """Resend welcome email to specific user

    Send a welcome email to a user. The contents of the welcome email can be set by [PATCH /accounts](#operation/updateAccount).

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param username: A username to send the welcome email to.
    :type username: str

    """
    return web.Response(status=200)
