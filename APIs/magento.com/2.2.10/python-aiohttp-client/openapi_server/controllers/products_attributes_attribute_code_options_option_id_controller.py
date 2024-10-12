from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_option_management_v1_delete_delete(request: web.Request, attribute_code, option_id) -> web.Response:
    """products/attributes/{attributeCode}/options/{optionId}

    Delete option from attribute

    :param attribute_code: 
    :type attribute_code: str
    :param option_id: 
    :type option_id: str

    """
    return web.Response(status=200)
