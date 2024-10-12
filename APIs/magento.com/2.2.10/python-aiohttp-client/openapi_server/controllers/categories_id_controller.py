from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_category_repository_v1_save_post_request import CatalogCategoryRepositoryV1SavePostRequest
from openapi_server.models.catalog_data_category_interface import CatalogDataCategoryInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """categories/{id}

    Create category service

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogCategoryRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
