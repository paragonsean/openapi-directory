# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_params import BadParams
from openapi_server.models.customer_additional_field import CustomerAdditionalField
from openapi_server.models.customer_additional_field_edit import CustomerAdditionalFieldEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_customers_id_fields_field_id_delete(client):
    """Test case for customers_id_fields_field_id_delete

    Delete a Customer Additional Field.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/customers/{id}/fields/{field_id}'.format(id=56, field_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_fields_field_id_get(client):
    """Test case for customers_id_fields_field_id_get

    Retrieve a single Customer Additional Field.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customers/{id}/fields/{field_id}'.format(id=56, field_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_fields_field_id_put(client):
    """Test case for customers_id_fields_field_id_put

    Update a Customer Additional Field.
    """
    body = {"customer_additional_field":{"value":"value","checkout_custom_field_id":0}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/customers/{id}/fields/{field_id}'.format(id=56, field_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_fields_get(client):
    """Test case for customers_id_fields_get

    Retrieves the Customer Additional Field of a Customer.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customers/{id}/fields'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_fields_post(client):
    """Test case for customers_id_fields_post

    Adds Customer Additional Fields to a Customer.
    """
    body = {"customer_additional_field":{"value":"value","checkout_custom_field_id":0}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/customers/{id}/fields'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

