from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server.models.catalog_product_custom_option_repository_v1_save_post_request import CatalogProductCustomOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_custom_option_repository_v1_save_put(request: web.Request, option_id, body=None) -> web.Response:
    """products/options/{optionId}

    Save Custom Option

    :param option_id: 
    :type option_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CatalogProductCustomOptionRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
