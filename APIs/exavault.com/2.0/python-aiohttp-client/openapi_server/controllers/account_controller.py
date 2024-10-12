from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.update_account_request_body import UpdateAccountRequestBody
from openapi_server import util


async def get_account(request: web.Request, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get account settings

    Get settings for your account, such as current space usage, webhooks settings, welcome email content and IP address restrictions.

    :param ev_api_key: API Key required for the request
    :type ev_api_key: str
    :param ev_access_token: Access Token for the request
    :type ev_access_token: str
    :param include: Related records to include in the response. Valid option is **masterUser**
    :type include: str

    """
    return web.Response(status=200)


async def update_account(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Update account settings

    Update account settings, such as welcome email content, IP address restrictions, webhooks settings and secure password requirements.  **Notes**  - You must have [admin-level access](/docs/account/04-users/00-introduction#managing-user-roles-and-permissions) to change account settings.

    :param ev_api_key: API Key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: Update Account Settings
    :type body: dict | bytes

    """
    body = UpdateAccountRequestBody.from_dict(body)
    return web.Response(status=200)
