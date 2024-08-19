from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def auth_oauth_token_post(request: web.Request, client_id, client_secret, grant_type, scope) -> web.Response:
    """Send client credentials and get an access token.

    

    :param client_id: Your app&#39;s client_id. Get from API dashboard.
    :type client_id: str
    :param client_secret: Your app&#39;s client_secret. Get from API dashboard.
    :type client_secret: str
    :param grant_type: Grant Type.
    :type grant_type: str
    :param scope: The resources that you would like to access.
    :type scope: str

    """
    return web.Response(status=200)
