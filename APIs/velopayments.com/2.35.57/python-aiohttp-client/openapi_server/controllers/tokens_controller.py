from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.resend_token_request import ResendTokenRequest
from openapi_server import util


async def resend_token(request: web.Request, user_id, body) -> web.Response:
    """Resend a token

    &lt;p&gt;Resend the specified token &lt;/p&gt; &lt;p&gt;The token to resend must already exist for the user &lt;/p&gt; &lt;p&gt;It will be revoked and a new one issued&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str
    :param body: The type of token to resend
    :type body: dict | bytes

    """
    body = ResendTokenRequest.from_dict(body)
    return web.Response(status=200)
