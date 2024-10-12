from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_product_request import CreateProductRequest
from openapi_server.models.product_model import ProductModel
from openapi_server.models.product_model_haljson import ProductModelHaljson
from openapi_server.models.update_product_request import UpdateProductRequest
from openapi_server import util


async def create_product(request: web.Request, organization_id, body) -> web.Response:
    """Create Product

    This endpoint creates a new Product in a specified Organization  identified by the &#x60;organizationId&#x60; parameter, which can be obtained from the [List Organizations](#operation/get-organizations) endpoint.

    :param organization_id: The identifier of the Organization.
    :type organization_id: str
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateProductRequest.from_dict(body)
    return web.Response(status=200)


async def delete_product(request: web.Request, product_id) -> web.Response:
    """Delete Product

    This endpoint removes a Product identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def get_product(request: web.Request, product_id) -> web.Response:
    """Get Product

    This endpoint returns the metadata of a Product  identified by the &#x60;productId&#x60;.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def get_products(request: web.Request, ) -> web.Response:
    """List Products

    This endpoint returns the list of the Products that belongs to the user.


    """
    return web.Response(status=200)


async def update_product(request: web.Request, product_id, body) -> web.Response:
    """Update Product

    This endpoint updates a Product identified by the &#x60;productId&#x60; parameter.

    :param product_id: The identifier of the Product.
    :type product_id: str
    :type product_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateProductRequest.from_dict(body)
    return web.Response(status=200)
