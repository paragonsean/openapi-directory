from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v1_accounts_post_request import ApiV1AccountsPostRequest
from openapi_server import util


async def api_v1_accounts_post(request: web.Request, body=None) -> web.Response:
    """api_v1_accounts_post

    Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiV1AccountsPostRequest.from_dict(body)
    return web.Response(status=200)
