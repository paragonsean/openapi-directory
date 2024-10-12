from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_interface import CatalogDataProductAttributeInterface
from openapi_server.models.catalog_product_attribute_repository_v1_save_post_request import CatalogProductAttributeRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_repository_v1_delete_by_id_delete(request: web.Request, attribute_code) -> web.Response:
    """products/attributes/{attributeCode}

    Delete Attribute by id

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)


async def catalog_product_attribute_repository_v1_get_get(request: web.Request, attribute_code) -> web.Response:
    """products/attributes/{attributeCode}

    Retrieve specific attribute

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)


async def catalog_product_attribute_repository_v1_save_put(request: web.Request, attribute_code, body=None) -> web.Response:
    """products/attributes/{attributeCode}

    Save attribute data

    :param attribute_code: 
    :type attribute_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
