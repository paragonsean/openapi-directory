from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.project_custom_field_attributes_get200_response import ProjectCustomFieldAttributesGet200Response
from openapi_server.models.project_custom_field_attributes_project_custom_field_attribute_id_get200_response import ProjectCustomFieldAttributesProjectCustomFieldAttributeIdGet200Response
from openapi_server import util


async def project_custom_field_attributes_get(request: web.Request, ) -> web.Response:
    """Get a list of project custom field attributes

    


    """
    return web.Response(status=200)


async def project_custom_field_attributes_project_custom_field_attribute_id_get(request: web.Request, project_custom_field_attribute_id) -> web.Response:
    """Details of 1 project custom field attribute

    

    :param project_custom_field_attribute_id: 
    :type project_custom_field_attribute_id: str

    """
    return web.Response(status=200)
