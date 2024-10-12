from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_category_attribute_interface import CatalogDataCategoryAttributeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_attribute_repository_v1_get_get(request: web.Request, attribute_code) -> web.Response:
    """categories/attributes/{attributeCode}

    Retrieve specific attribute

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)
