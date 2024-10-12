# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_patch import CustomerPatch
from openapi_server.models.customer_post import CustomerPost
from openapi_server.models.order import Order


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_customer(client):
    """Test case for create_customer

    Create a new customer in eCommerce system.With the exception of the 'id' field, the required fields indicated in the 'Customer' model are those required to create a new customer
    """
    customer = openapi_server.CustomerPost()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='POST',
        path='/elements/api-v2/customers',
        headers=headers,
        json=customer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_customer_by_id(client):
    """Test case for delete_customer_by_id

    Delete a customer associated with a given ID from your eCommerce system. Specifying a customer associated with a given ID that does not exist will result in an error message
    """
    headers = { 
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='DELETE',
        path='/elements/api-v2/customers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customer_by_id(client):
    """Test case for get_customer_by_id

    Retrieve a customer associated with a given ID from the eCommerce system. Specifying a customer with an ID that does not exist will result in an error response
    """
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/customers/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customers(client):
    """Test case for get_customers

    Find customers in the eCommerce system, using the provided CEQL search expression. If no search expression is provided, all records will be retrieved
    """
    params = [('where', 'where_example'),
                    ('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_customers_orders(client):
    """Test case for get_customers_orders

    Find orders in the customer associated with a given ID. If the customer does not exist, an error response will be returned. If no orders are found in the given customer then an empty array will be returned
    """
    params = [('pageSize', 56),
                    ('nextPage', 'next_page_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': '*/*',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='GET',
        path='/elements/api-v2/customers/{id}/orders'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_customer_by_id(client):
    """Test case for update_customer_by_id

    Update an customer associated with a given ID in the eCommerce system.The update API uses the PATCH HTTP verb, so only those fields provided in the customer object will be updated, and those fields not provided will be left alone. Updating a customer with a specified ID that does not exist will result in an error response
    """
    customer = openapi_server.CustomerPatch()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'authorization': 'authorization_example',
    }
    response = await client.request(
        method='PATCH',
        path='/elements/api-v2/customers/{id}'.format(id='id_example'),
        headers=headers,
        json=customer,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

