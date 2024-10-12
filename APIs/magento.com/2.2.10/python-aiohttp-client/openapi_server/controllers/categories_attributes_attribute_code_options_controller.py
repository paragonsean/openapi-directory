from typing import List, Dict
from aiohttp import web

from openapi_server.models.eav_data_attribute_option_interface import EavDataAttributeOptionInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_category_attribute_option_management_v1_get_items_get(request: web.Request, attribute_code) -> web.Response:
    """categories/attributes/{attributeCode}/options

    Retrieve list of attribute options

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)
