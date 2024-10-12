from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_category_management_v1_assign_categories_post_request import SharedCatalogCategoryManagementV1AssignCategoriesPostRequest
from openapi_server import util


async def shared_catalog_category_management_v1_assign_categories_post(request: web.Request, id, body=None) -> web.Response:
    """sharedCatalog/{id}/assignCategories

    Add categories into the shared catalog.

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SharedCatalogCategoryManagementV1AssignCategoriesPostRequest.from_dict(body)
    return web.Response(status=200)
