from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_address_metadata_v1_get_attribute_metadata_get(request: web.Request, attribute_code) -> web.Response:
    """attributeMetadata/customerAddress/attribute/{attributeCode}

    Retrieve attribute metadata.

    :param attribute_code: 
    :type attribute_code: str

    """
    return web.Response(status=200)
