from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.form_fields_form_field_id_get200_response import FormFieldsFormFieldIdGet200Response
from openapi_server.models.form_fields_post_request import FormFieldsPostRequest
from openapi_server import util


async def form_fields_form_field_id_get(request: web.Request, form_field_id) -> web.Response:
    """Get details about single &#x60;FormField&#x60;

    

    :param form_field_id: 
    :type form_field_id: str

    """
    return web.Response(status=200)


async def form_fields_post(request: web.Request, body=None) -> web.Response:
    """Add a new field to a &#x60;Form&#x60;

    

    :param body: 
    :type body: dict | bytes

    """
    body = FormFieldsPostRequest.from_dict(body)
    return web.Response(status=200)
