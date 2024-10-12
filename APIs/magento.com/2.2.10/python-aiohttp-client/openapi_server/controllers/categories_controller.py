from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_category_repository_v1_save_post_request import CatalogCategoryRepositoryV1SavePostRequest
from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.catalog_data_category_tree_interface import CatalogDataCategoryTreeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_management_v1_get_tree_get(request: web.Request, root_category_id=None, depth=None) -> web.Response:
    """categories

    Retrieve list of categories

    :param root_category_id: 
    :type root_category_id: int
    :param depth: 
    :type depth: int

    """
    return web.Response(status=200)


async def catalog_category_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """categories

    Create category service

    :param body: 
    :type body: dict | bytes

    """
    body = CatalogCategoryRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
