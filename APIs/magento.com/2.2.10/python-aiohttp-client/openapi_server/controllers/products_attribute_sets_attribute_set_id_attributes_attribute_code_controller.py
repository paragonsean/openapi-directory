from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_management_v1_unassign_delete(request: web.Request, attribute_set_id, attribute_code) -> web.Response:
    """products/attribute-sets/{attributeSetId}/attributes/{attributeCode}

    Remove attribute from attribute set

    :param attribute_set_id: 
    :type attribute_set_id: str
    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)
