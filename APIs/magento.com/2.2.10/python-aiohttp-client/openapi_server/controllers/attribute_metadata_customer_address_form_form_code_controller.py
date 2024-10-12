from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_address_metadata_v1_get_attributes_get(request: web.Request, form_code) -> web.Response:
    """attributeMetadata/customerAddress/form/{formCode}

    Retrieve all attributes filtered by form code

    :param form_code: 
    :type form_code: str

    """
    return web.Response(status=200)
