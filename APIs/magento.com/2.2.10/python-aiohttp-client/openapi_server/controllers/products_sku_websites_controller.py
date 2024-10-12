from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_product_website_link_repository_v1_save_put_request import CatalogProductWebsiteLinkRepositoryV1SavePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_website_link_repository_v1_save_post(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/websites

    Assign a product to the website

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductWebsiteLinkRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_product_website_link_repository_v1_save_put(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/websites

    Assign a product to the website

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductWebsiteLinkRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
