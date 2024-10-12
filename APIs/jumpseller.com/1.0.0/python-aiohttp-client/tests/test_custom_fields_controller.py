# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_field import CustomField
from openapi_server.models.custom_field_edit import CustomFieldEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_json_delete(client):
    """Test case for custom_fields_id_json_delete

    Delete an existing CustomField.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_json_get(client):
    """Test case for custom_fields_id_json_get

    Retrieve a single CustomField.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_json_put(client):
    """Test case for custom_fields_id_json_put

    Update a CustomField.
    """
    body = {"custom_field":{"values":["values","values"],"label":"label","type":"text"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_id_select_options_custom_field_select_option_id_json_delete(client):
    """Test case for custom_fields_id_select_options_custom_field_select_option_id_json_delete

    Delete an existing CustomFieldSelectOption.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/custom_fields/{id}/select_options/{custom_field_select_option_id_jso}'.format(id=56, custom_field_select_option_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_json_get(client):
    """Test case for custom_fields_json_get

    Retrieve all Store's Custom Fields.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/custom_fields.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_json_post(client):
    """Test case for custom_fields_json_post

    Create a new Custom Field.
    """
    body = {"custom_field":{"values":["values","values"],"label":"label","type":"text"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/custom_fields.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

