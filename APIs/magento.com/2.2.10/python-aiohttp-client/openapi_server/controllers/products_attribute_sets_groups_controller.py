from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_product_attribute_group_repository_v1_save_post_request import CatalogProductAttributeGroupRepositoryV1SavePostRequest
from openapi_server.models.eav_data_attribute_group_interface import EavDataAttributeGroupInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_group_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """products/attribute-sets/groups

    Save attribute group

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeGroupRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
