from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_interface import CatalogDataProductInterface
from openapi_server.models.catalog_product_repository_v1_save_post_request import CatalogProductRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_repository_v1_delete_by_id_delete(request: web.Request, sku) -> web.Response:
    """products/{sku}

    

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)


async def catalog_product_repository_v1_get_get(request: web.Request, sku, edit_mode=None, store_id=None, force_reload=None) -> web.Response:
    """products/{sku}

    Get info about product by product SKU

    :param sku: 
    :type sku: str
    :param edit_mode: 
    :type edit_mode: bool
    :param store_id: 
    :type store_id: int
    :param force_reload: 
    :type force_reload: bool

    """
    return web.Response(status=200)


async def catalog_product_repository_v1_save_put(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}

    Create product

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
