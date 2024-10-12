from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_product_link_management_v1_set_product_links_post_request import CatalogProductLinkManagementV1SetProductLinksPostRequest
from openapi_server.models.catalog_product_link_repository_v1_save_put_request import CatalogProductLinkRepositoryV1SavePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_link_management_v1_set_product_links_post(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/links

    Assign a product link to another product

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductLinkManagementV1SetProductLinksPostRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_product_link_repository_v1_save_put(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/links

    Save product link

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductLinkRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
