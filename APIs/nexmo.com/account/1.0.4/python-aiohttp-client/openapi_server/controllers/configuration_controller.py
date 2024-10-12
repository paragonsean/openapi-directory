from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_settings import AccountSettings
from openapi_server.models.register_email_request import RegisterEmailRequest
from openapi_server.models.register_email_response import RegisterEmailResponse
from openapi_server import util


async def change_account_settings(request: web.Request, api_key, api_secret, dr_call_back_url=None, mo_call_back_url=None) -> web.Response:
    """Change Account Settings

    Update the default webhook URLs associated with your account:   * Callback URL for incoming SMS messages   * Callback URL for delivery receipts  Note that the URLs you provide must be valid and active. Vonage will check that they return a 200 OK response before the setting is saved.

    :param api_key: Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param dr_call_back_url: The webhook URL that Vonage makes a request to when a delivery receipt is available  for an SMS sent by one of your Vonage numbers. Send an empty string to unset this value.
    :type dr_call_back_url: str
    :param mo_call_back_url: The default webhook URL for inbound SMS. If an SMS is received at a Vonage number  that does not have its own inbound SMS webhook configured, Vonage makes a request here. Send an empty string to unset this value.
    :type mo_call_back_url: str

    """
    return web.Response(status=200)


async def register_sender(request: web.Request, api_key, api_secret, body) -> web.Response:
    """Register an email sender

    Register an email sender with an API Key for using email with Verify V2.

    :param api_key: Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = RegisterEmailRequest.from_dict(body)
    return web.Response(status=200)
