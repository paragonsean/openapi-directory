from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.product import Product
from openapi_server.models.product_list import ProductList
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def create_product(request: web.Request, body) -> web.Response:
    """Create a product

    Create a new product. Returns a product object if the create is succeded.

    :param body: Product object that you would like to store.
    :type body: dict | bytes

    """
    body = Product.from_dict(body)
    return web.Response(status=200)


async def delete_product(request: web.Request, id) -> web.Response:
    """Delete a product

    Delete an existing product.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_product(request: web.Request, id) -> web.Response:
    """Retrieve a product

    Retrieves the details of an existing product.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def list_product(request: web.Request, page=None, per_page=None) -> web.Response:
    """List all product

    Returns a list of your products. The partners are returned sorted by creation date, with the most recent partners appearing first.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def update_product(request: web.Request, id, body) -> web.Response:
    """Update a product

    Update an existing product. Returns a product object if the update is succeded.

    :param id: 
    :type id: int
    :param body: Product object that you would like to update.
    :type body: dict | bytes

    """
    body = Product.from_dict(body)
    return web.Response(status=200)
