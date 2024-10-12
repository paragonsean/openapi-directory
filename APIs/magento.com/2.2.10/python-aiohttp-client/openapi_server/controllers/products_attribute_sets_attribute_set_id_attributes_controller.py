from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_interface import CatalogDataProductAttributeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_management_v1_get_attributes_get(request: web.Request, attribute_set_id) -> web.Response:
    """products/attribute-sets/{attributeSetId}/attributes

    Retrieve related attributes based on given attribute set ID

    :param attribute_set_id: 
    :type attribute_set_id: str

    """
    return web.Response(status=200)
