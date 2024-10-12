from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_slug_request import CreateSlugRequest
from openapi_server.models.slug_response import SlugResponse
from openapi_server import util


async def create_product_slug(request: web.Request, organization_uuid, body) -> web.Response:
    """Create a product identifier

    Creates a unique slug (identifier) for a product. The slug is used to create a product URL

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSlugRequest.from_dict(body)
    return web.Response(status=200)
