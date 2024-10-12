from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_balance import ApiV2010AccountBalance
from openapi_server import util


async def fetch_balance(request: web.Request, account_sid) -> web.Response:
    """fetch_balance

    Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately. Child accounts do not contain balance information

    :param account_sid: The unique SID identifier of the Account.
    :type account_sid: str

    """
    return web.Response(status=200)
