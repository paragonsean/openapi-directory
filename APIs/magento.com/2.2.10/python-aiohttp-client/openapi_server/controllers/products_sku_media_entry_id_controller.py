from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_media_gallery_entry_interface import CatalogDataProductAttributeMediaGalleryEntryInterface
from openapi_server.models.catalog_product_attribute_media_gallery_management_v1_create_post_request import CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_media_gallery_management_v1_get_get(request: web.Request, sku, entry_id) -> web.Response:
    """products/{sku}/media/{entryId}

    Return information about gallery entry

    :param sku: 
    :type sku: str
    :param entry_id: 
    :type entry_id: int

    """
    return web.Response(status=200)


async def catalog_product_attribute_media_gallery_management_v1_remove_delete(request: web.Request, sku, entry_id) -> web.Response:
    """products/{sku}/media/{entryId}

    Remove gallery entry

    :param sku: 
    :type sku: str
    :param entry_id: 
    :type entry_id: int

    """
    return web.Response(status=200)


async def catalog_product_attribute_media_gallery_management_v1_update_put(request: web.Request, sku, entry_id, body=None) -> web.Response:
    """products/{sku}/media/{entryId}

    Update gallery entry

    :param sku: 
    :type sku: str
    :param entry_id: 
    :type entry_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeMediaGalleryManagementV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)
