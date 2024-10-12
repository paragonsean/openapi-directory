from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_view import ProductView
from openapi_server.models.products_api_count200_response import ProductsApiCount200Response
from openapi_server.models.products_api_count_request import ProductsApiCountRequest
from openapi_server.models.products_api_find200_response import ProductsApiFind200Response
from openapi_server.models.products_api_find_request import ProductsApiFindRequest
from openapi_server.models.products_api_patch_product2_request import ProductsApiPatchProduct2Request
from openapi_server import util


async def products_api_count(request: web.Request, body) -> web.Response:
    """products_api_count

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiCountRequest.from_dict(body)
    return web.Response(status=200)


async def products_api_delete_product(request: web.Request, x_api_key, serial) -> web.Response:
    """products_api_delete_product

    

    :param x_api_key: 
    :type x_api_key: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def products_api_delete_product2(request: web.Request, x_api_key, serial) -> web.Response:
    """products_api_delete_product2

    

    :param x_api_key: 
    :type x_api_key: str
    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def products_api_find(request: web.Request, body, page=None) -> web.Response:
    """products_api_find

    

    :param body: 
    :type body: dict | bytes
    :param page: 
    :type page: int

    """
    body = ProductsApiFindRequest.from_dict(body)
    return web.Response(status=200)


async def products_api_list(request: web.Request, body, page=None) -> web.Response:
    """products_api_list

    

    :param body: 
    :type body: dict | bytes
    :param page: 
    :type page: int

    """
    body = ProductsApiCountRequest.from_dict(body)
    return web.Response(status=200)


async def products_api_patch_product(request: web.Request, body) -> web.Response:
    """products_api_patch_product

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiPatchProduct2Request.from_dict(body)
    return web.Response(status=200)


async def products_api_patch_product2(request: web.Request, body) -> web.Response:
    """products_api_patch_product2

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiPatchProduct2Request.from_dict(body)
    return web.Response(status=200)


async def products_api_save(request: web.Request, body) -> web.Response:
    """products_api_save

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsApiPatchProduct2Request.from_dict(body)
    return web.Response(status=200)
