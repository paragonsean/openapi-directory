from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_category_link_repository_v1_save_put_request import CatalogCategoryLinkRepositoryV1SavePutRequest
from openapi_server.models.catalog_data_category_product_link_interface import CatalogDataCategoryProductLinkInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_link_management_v1_get_assigned_products_get(request: web.Request, category_id) -> web.Response:
    """categories/{categoryId}/products

    Get products assigned to category

    :param category_id: 
    :type category_id: int

    """
    return web.Response(status=200)


async def catalog_category_link_repository_v1_save_post(request: web.Request, category_id, body=None) -> web.Response:
    """categories/{categoryId}/products

    Assign a product to the required category

    :param category_id: 
    :type category_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogCategoryLinkRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_category_link_repository_v1_save_put(request: web.Request, category_id, body=None) -> web.Response:
    """categories/{categoryId}/products

    Assign a product to the required category

    :param category_id: 
    :type category_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogCategoryLinkRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
