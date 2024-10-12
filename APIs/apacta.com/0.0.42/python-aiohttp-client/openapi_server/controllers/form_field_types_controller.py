from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.form_field_types_form_field_type_id_get200_response import FormFieldTypesFormFieldTypeIdGet200Response
from openapi_server.models.form_field_types_get200_response import FormFieldTypesGet200Response
from openapi_server import util


async def form_field_types_form_field_type_id_get(request: web.Request, form_field_type_id) -> web.Response:
    """Get details about single &#x60;FormField&#x60;

    

    :param form_field_type_id: 
    :type form_field_type_id: str

    """
    return web.Response(status=200)


async def form_field_types_get(request: web.Request, name=None, identifier=None) -> web.Response:
    """Get list of form field types

    

    :param name: Used to filter on the &#x60;name&#x60; of the form_fields
    :type name: str
    :param identifier: Used to filter on the &#x60;identifier&#x60; of the form_fields
    :type identifier: str

    """
    return web.Response(status=200)
