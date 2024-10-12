from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_product_rating200_response import GetProductRating200Response
from openapi_server import util


async def get_product_rating(request: web.Request, product_id, content_type, accept) -> web.Response:
    """Get Product Rating

    Retrieves the rating of a specific product.

    :param product_id: Product ID.
    :type product_id: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
