# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.form_field_types_form_field_type_id_get200_response import FormFieldTypesFormFieldTypeIdGet200Response
from openapi_server.models.form_field_types_get200_response import FormFieldTypesGet200Response


pytestmark = pytest.mark.asyncio

async def test_form_field_types_form_field_type_id_get(client):
    """Test case for form_field_types_form_field_type_id_get

    Get details about single `FormField`
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/form_field_types/{form_field_type_id}'.format(form_field_type_id='form_field_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_form_field_types_get(client):
    """Test case for form_field_types_get

    Get list of form field types
    """
    params = [('name', 'name_example'),
                    ('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/form_field_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

