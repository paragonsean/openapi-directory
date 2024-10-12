from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_get200_response import AccountGet200Response
from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.rate_limit import RateLimit
from openapi_server import util


async def account_get(request: web.Request, ) -> web.Response:
    """Fetch credit balance and free API calls.

    Get the current credit balance and number of free API calls.  Notes:  * Balance changes may be delayed by several seconds. To locally keep track of your credit balance, you should therefore only call this endpoint initially (or e.g. when the user manually triggers a refresh), then use the &#x60;X-Credits-Charged&#x60; response header returned with each image processing response to adjust the local balance.  * The \&quot;*sizes*\&quot; field is always \&quot;all\&quot;, is deprecated and will soon be removed. 


    """
    return web.Response(status=200)
