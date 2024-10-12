# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.customer_category import CustomerCategory
from openapi_server.models.customer_category_edit import CustomerCategoryEdit
from openapi_server.models.customers_to_customer_category import CustomersToCustomerCategory
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_customers_json_delete(client):
    """Test case for customer_categories_id_customers_json_delete

    Delete Customers from an existing CustomerCategory.
    """
    body = {"customers":[{"id":0,"email":"email"},{"id":0,"email":"email"}]}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/customer_categories/{id}/customers.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_customers_json_get(client):
    """Test case for customer_categories_id_customers_json_get

    Retrieves the customers in a CustomerCategory.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customer_categories/{id}/customers.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_customers_json_post(client):
    """Test case for customer_categories_id_customers_json_post

    Adds Customers to a CustomerCategory.
    """
    body = {"customers":[{"id":0,"email":"email"},{"id":0,"email":"email"}]}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/customer_categories/{id}/customers.json'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_json_delete(client):
    """Test case for customer_categories_id_json_delete

    Delete an existing CustomerCategory.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/customer_categories/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_json_get(client):
    """Test case for customer_categories_id_json_get

    Retrieve a single CustomerCategory.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customer_categories/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_id_json_put(client):
    """Test case for customer_categories_id_json_put

    Update a CustomerCategory.
    """
    body = {"category":{"name":"name"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/customer_categories/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_json_get(client):
    """Test case for customer_categories_json_get

    Retrieve all Customer Categories.
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
        path='/v1/customer_categories.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customer_categories_json_post(client):
    """Test case for customer_categories_json_post

    Create a new CustomerCategory.
    """
    body = {"category":{"name":"name"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/customer_categories.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

