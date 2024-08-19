# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checkout_custom_field import CheckoutCustomField
from openapi_server.models.checkout_custom_field_edit import CheckoutCustomFieldEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_checkout_custom_fields_id_json_delete(client):
    """Test case for checkout_custom_fields_id_json_delete

    Delete an existing CheckoutCustomField.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/checkout_custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checkout_custom_fields_id_json_get(client):
    """Test case for checkout_custom_fields_id_json_get

    Retrieve a single CheckoutCustomField.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/checkout_custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checkout_custom_fields_id_json_put(client):
    """Test case for checkout_custom_fields_id_json_put

    Update a CheckoutCustomField.
    """
    body = {"checkout_custom_field":{"area":"contact","deletable":False,"label":"label","position":0,"type":"text","custom_field_select_options":["custom_field_select_options","custom_field_select_options"],"required":False}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/checkout_custom_fields/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checkout_custom_fields_json_get(client):
    """Test case for checkout_custom_fields_json_get

    Retrieve all Checkout Custom Fields.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('limit', 50),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/checkout_custom_fields.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_checkout_custom_fields_json_post(client):
    """Test case for checkout_custom_fields_json_post

    Create a new CheckoutCustomField.
    """
    body = {"checkout_custom_field":{"area":"contact","deletable":False,"label":"label","position":0,"type":"text","custom_field_select_options":["custom_field_select_options","custom_field_select_options"],"required":False}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/checkout_custom_fields.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

