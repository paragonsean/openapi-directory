from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_address_metadata_v1_get_custom_attributes_metadata_get(request: web.Request, data_interface_name=None) -> web.Response:
    """attributeMetadata/customerAddress/custom

    Get custom attributes metadata for the given data interface.

    :param data_interface_name: 
    :type data_interface_name: str

    """
    return web.Response(status=200)
