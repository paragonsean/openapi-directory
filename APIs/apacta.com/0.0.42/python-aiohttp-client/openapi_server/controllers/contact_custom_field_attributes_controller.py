from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_custom_field_attributes_contact_custom_field_attribute_id_get200_response import ContactCustomFieldAttributesContactCustomFieldAttributeIdGet200Response
from openapi_server.models.contact_custom_field_attributes_get200_response import ContactCustomFieldAttributesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def contact_custom_field_attributes_contact_custom_field_attribute_id_get(request: web.Request, contact_custom_field_attribute_id) -> web.Response:
    """Details of 1 contact custom field attribute

    

    :param contact_custom_field_attribute_id: 
    :type contact_custom_field_attribute_id: str

    """
    return web.Response(status=200)


async def contact_custom_field_attributes_get(request: web.Request, ) -> web.Response:
    """Get a list of contact custom field attributes

    


    """
    return web.Response(status=200)
