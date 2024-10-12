from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_token import ApiV2010AccountToken
from openapi_server import util


async def create_token(request: web.Request, account_sid, ttl=None) -> web.Response:
    """create_token

    Create a new token for ICE servers

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).
    :type ttl: int

    """
    return web.Response(status=200)
