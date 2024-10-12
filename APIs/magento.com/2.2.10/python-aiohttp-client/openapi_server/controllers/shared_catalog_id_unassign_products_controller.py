from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_product_management_v1_assign_products_post_request import SharedCatalogProductManagementV1AssignProductsPostRequest
from openapi_server import util


async def shared_catalog_product_management_v1_unassign_products_post(request: web.Request, id, body=None) -> web.Response:
    """sharedCatalog/{id}/unassignProducts

    Remove the specified products from the shared catalog.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SharedCatalogProductManagementV1AssignProductsPostRequest.from_dict(body)
    return web.Response(status=200)
