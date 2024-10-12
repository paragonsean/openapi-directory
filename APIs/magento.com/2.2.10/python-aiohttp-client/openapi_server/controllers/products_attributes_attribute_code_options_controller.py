from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_product_attribute_option_management_v1_add_post_request import CatalogProductAttributeOptionManagementV1AddPostRequest
from openapi_server.models.eav_data_attribute_option_interface import EavDataAttributeOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_option_management_v1_add_post(request: web.Request, attribute_code, body=None) -> web.Response:
    """products/attributes/{attributeCode}/options

    Add option to attribute

    :param attribute_code: 
    :type attribute_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeOptionManagementV1AddPostRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_product_attribute_option_management_v1_get_items_get(request: web.Request, attribute_code) -> web.Response:
    """products/attributes/{attributeCode}/options

    Retrieve list of attribute options

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)
