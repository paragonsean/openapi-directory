from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_token_response import UserTokenResponse
from openapi_server import util


async def usertoken_get(request: web.Request, fid, auth_info) -> web.Response:
    """Returns User Session Token

    This resource creates the user session. It must be called prior to any other API calls for the specified user. The Token value does not expire. 

    :param fid: Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    :type fid: str
    :param auth_info: Authorization Information. AES 128-bit encrypted concatenation of \&quot;User ID as specified in enrollment:FI ID as provided by Mastercard:current Unix time\&quot;. Key exchange and establishment of maintenance procedures occur during implementation.
    :type auth_info: str

    """
    return web.Response(status=200)
