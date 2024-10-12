from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server import util


async def get_account(request: web.Request, ) -> web.Response:
    """Get information about account

    Retrieves information from an account, such as company and sponsor user details, stores, and appTokens.    This endpoint only accepts requests from the host list designated for that store. If you want to try this request from this portal, be sure to add it to the list. Learn how to add hosts to the list in [How to manage accounts](https://help.vtex.com/en/tutorial/how-to-manage-accounts--tutorials_6285#).


    """
    return web.Response(status=200)
