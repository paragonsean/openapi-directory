from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_product_attribute_management_v1_assign_post_request import CatalogProductAttributeManagementV1AssignPostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_management_v1_assign_post(request: web.Request, body=None) -> web.Response:
    """products/attribute-sets/attributes

    Assign attribute to attribute set

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductAttributeManagementV1AssignPostRequest.from_dict(body)
    return web.Response(status=200)
