from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_data_product_attribute_interface import CatalogDataProductAttributeInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_media_attribute_management_v1_get_list_get(request: web.Request, attribute_set_name) -> web.Response:
    """products/media/types/{attributeSetName}

    Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.

    :param attribute_set_name: 
    :type attribute_set_name: str

    """
    return web.Response(status=200)
