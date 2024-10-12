from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_category_management_v1_move_put_request import CatalogCategoryManagementV1MovePutRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_management_v1_move_put(request: web.Request, category_id, body=None) -> web.Response:
    """categories/{categoryId}/move

    Move category

    :param category_id: 
    :type category_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogCategoryManagementV1MovePutRequest.from_dict(body)
    return web.Response(status=200)
