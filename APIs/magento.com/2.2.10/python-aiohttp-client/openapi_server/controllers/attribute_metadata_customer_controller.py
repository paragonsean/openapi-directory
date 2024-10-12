from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_customer_metadata_v1_get_all_attributes_metadata_get(request: web.Request, ) -> web.Response:
    """attributeMetadata/customer

    Get all attribute metadata.


    """
    return web.Response(status=200)
