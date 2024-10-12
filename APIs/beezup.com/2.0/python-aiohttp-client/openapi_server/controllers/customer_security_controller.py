from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.zendesk_token import ZendeskToken
from openapi_server import util


async def logout(request: web.Request, ) -> web.Response:
    """Log out the current user from go2

    Log out the current user from go2


    """
    return web.Response(status=200)


async def zendesk_token(request: web.Request, ) -> web.Response:
    """Zendesk token

    Zendesk token - Generates a JWT token to access BeezUP restricted Help Center in SSO as described here: https://support.zendesk.com/hc/en-us/articles/222874768-Using-restricted-Help-Center-content-with-the-Web-Widget


    """
    return web.Response(status=200)
