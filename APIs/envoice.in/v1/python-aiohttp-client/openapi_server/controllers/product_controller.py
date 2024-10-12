from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_result_product_details_api_model import ListResultProductDetailsApiModel
from openapi_server.models.product_create_api_model import ProductCreateApiModel
from openapi_server.models.product_delete_api_model import ProductDeleteApiModel
from openapi_server.models.product_full_details_api_model import ProductFullDetailsApiModel
from openapi_server.models.product_update_api_model import ProductUpdateApiModel
from openapi_server import util


async def product_api_all(request: web.Request, x_auth_key, x_auth_secret, query_options_page=None, query_options_page_size=None) -> web.Response:
    """Return all products for the account

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param query_options_page: 
    :type query_options_page: int
    :param query_options_page_size: 
    :type query_options_page_size: int

    """
    return web.Response(status=200)


async def product_api_delete(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Delete an existing product

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProductDeleteApiModel.from_dict(body)
    return web.Response(status=200)


async def product_api_details(request: web.Request, id, x_auth_key, x_auth_secret) -> web.Response:
    """Return product details

    

    :param id: 
    :type id: int
    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)


async def product_api_new(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Create a product

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProductCreateApiModel.from_dict(body)
    return web.Response(status=200)


async def product_api_update(request: web.Request, x_auth_key, x_auth_secret, body) -> web.Response:
    """Update an existing product

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProductUpdateApiModel.from_dict(body)
    return web.Response(status=200)
