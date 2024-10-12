from typing import List, Dict
from aiohttp import web

from openapi_server.models.apiv10_safe_unsafe_image_with_tags_body import Apiv10SafeUnsafeImageWithTagsBody
from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server import util


async def api_v10_safe_unsafe_image_with_tags_post(request: web.Request, body=None) -> web.Response:
    """api_v10_safe_unsafe_image_with_tags_post

    Auto generated using Swagger Inspector

    :param body: 
    :type body: dict | bytes

    """
    body = Apiv10SafeUnsafeImageWithTagsBody.from_dict(body)
    return web.Response(status=200)
