from typing import List, Dict
from aiohttp import web

from openapi_server.models.products_reviews_id_put_request import ProductsReviewsIdPutRequest
from openapi_server import util


async def products_reviews_id_get(request: web.Request, id) -> web.Response:
    """View a review

    View a review

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def products_reviews_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a review

    Update a review

    :param id: 
    :type id: str
    :param body: the content of the request
    :type body: dict | bytes

    """
    body = ProductsReviewsIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def products_slug_reviews_get(request: web.Request, slug) -> web.Response:
    """View reviews of a comparison shopping page

    View reviews of a comparison shopping page

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def products_slug_reviews_post(request: web.Request, slug) -> web.Response:
    """Create a review for a product

    Create a review for a product

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)
