from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_media_gallery_entry_interface import CatalogDataProductAttributeMediaGalleryEntryInterface
from openapi_server.models.catalog_product_attribute_media_gallery_management_v1_create_post_request import CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_media_gallery_management_v1_create_post(request: web.Request, sku, body=None) -> web.Response:
    """products/{sku}/media

    Create new gallery entry

    :param sku: 
    :type sku: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_product_attribute_media_gallery_management_v1_get_list_get(request: web.Request, sku) -> web.Response:
    """products/{sku}/media

    Retrieve the list of gallery entries associated with given product

    :param sku: 
    :type sku: str

    """
    return web.Response(status=200)
