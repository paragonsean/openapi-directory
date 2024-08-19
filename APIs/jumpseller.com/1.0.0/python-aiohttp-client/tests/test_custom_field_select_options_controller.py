# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field_select_option import CustomFieldSelectOption
from openapi_server.models.custom_field_select_option_edit import CustomFieldSelectOptionEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_select_options_custom_field_select_option_id_json_get(client):
    """Test case for custom_fields_id_select_options_custom_field_select_option_id_json_get

    Retrieve a single SelectOption from a CustomField.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/custom_fields/{id}/select_options/{custom_field_select_option_id_jso}'.format(id=56, custom_field_select_option_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_select_options_custom_field_select_option_id_json_put(client):
    """Test case for custom_fields_id_select_options_custom_field_select_option_id_json_put

    Update a SelectOption from a CustomField.
    """
    body = {"custom_field_select_option":{"value":"value"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/custom_fields/{id}/select_options/{custom_field_select_option_id_jso}'.format(id=56, custom_field_select_option_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_select_options_json_get(client):
    """Test case for custom_fields_id_select_options_json_get

    Retrieve all Store's Custom Fields.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/custom_fields/{id}/select_options.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_select_options_json_post(client):
    """Test case for custom_fields_id_select_options_json_post

    Create a new Custom Field Select Option.
    """
    body = {"custom_field_select_option":{"value":"value"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/custom_fields/{id}/select_options.json'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

