from typing import List, Dict
from aiohttp import web

from openapi_server.models.post_token200_response import PostToken200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.post_token_request import PostTokenRequest
from openapi_server import util


async def post_token(request: web.Request, content_type, authorization, body=None) -> web.Response:
    """Get authentication token

    This endpoint allows you to get an authentication token. No need to be authenticated to use this endpoint.

    :param content_type: Equal to &#39;application/json&#39; or &#39;application/x-www-form-urlencoded&#39;, no other value allowed
    :type content_type: str
    :param authorization: Equal to &#39;Basic xx&#39;, where &#39;xx&#39; is the base 64 encoding of the client id and secret. Find out how to generate them in the &lt;a href&#x3D;\&quot;/documentation/authentication.html#client-idsecret-generation\&quot;&gt;Client ID/secret generation&lt;/a&gt; section.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PostTokenRequest.from_dict(body)
    return web.Response(status=200)
