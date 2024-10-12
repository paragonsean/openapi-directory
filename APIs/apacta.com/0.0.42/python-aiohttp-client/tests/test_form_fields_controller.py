# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.form_fields_form_field_id_get200_response import FormFieldsFormFieldIdGet200Response
from openapi_server.models.form_fields_post_request import FormFieldsPostRequest


pytestmark = pytest.mark.asyncio

async def test_form_fields_form_field_id_get(client):
    """Test case for form_fields_form_field_id_get

    Get details about single `FormField`
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/form_fields/{form_field_id}'.format(form_field_id='form_field_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_form_fields_post(client):
    """Test case for form_fields_post

    Add a new field to a `Form`
    """
    body = openapi_server.FormFieldsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/form_fields',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

