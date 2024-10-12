from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_attribute_set_management_v1_create_post_request import CatalogAttributeSetManagementV1CreatePostRequest
from openapi_server.models.eav_data_attribute_set_interface import EavDataAttributeSetInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_attribute_set_management_v1_create_post(request: web.Request, body=None) -> web.Response:
    """products/attribute-sets

    Create attribute set from data

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogAttributeSetManagementV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)
