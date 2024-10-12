from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.user_custom_field_attributes_get200_response import UserCustomFieldAttributesGet200Response
from openapi_server.models.user_custom_field_attributes_user_custom_field_attribute_id_get200_response import UserCustomFieldAttributesUserCustomFieldAttributeIdGet200Response
from openapi_server import util


async def user_custom_field_attributes_get(request: web.Request, ) -> web.Response:
    """Get a list of user custom field attributes

    


    """
    return web.Response(status=200)


async def user_custom_field_attributes_user_custom_field_attribute_id_get(request: web.Request, user_custom_field_attribute_id) -> web.Response:
    """Details of 1 user custom field attribute

    

    :param user_custom_field_attribute_id: 
    :type user_custom_field_attribute_id: str

    """
    return web.Response(status=200)
