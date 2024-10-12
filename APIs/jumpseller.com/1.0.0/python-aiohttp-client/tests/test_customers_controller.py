# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.customer import Customer
from openapi_server.models.customer_with_password_no_id import CustomerWithPasswordNoID
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_customers_count_json_get(client):
    """Test case for customers_count_json_get

    Count all Customers.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customers/count.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_email_email_json_get(client):
    """Test case for customers_email_email_json_get

    Retrieve a single Customer by email.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customers/email/{email_jso}'.format(email='email_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_json_delete(client):
    """Test case for customers_id_json_delete

    Delete an existing Customer.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/customers/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_json_get(client):
    """Test case for customers_id_json_get

    Retrieve a single Customer by id.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/customers/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_id_json_put(client):
    """Test case for customers_id_json_put

    Update a new Customer.
    """
    body = {"customer":{"password":"password","phone":"phone","billing_address":{"country":"country","address":"address","city":"city","surname":"surname","taxid":"taxid","municipality":"municipality","name":"name","postal":"postal","region":"region"},"customer_category":[0,0],"shipping_address":{"country":"country","address":"address","city":"city","surname":"surname","municipality":"municipality","name":"name","postal":"postal","region":"region"},"email":"email","status":"approved"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/customers/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_json_get(client):
    """Test case for customers_json_get

    Retrieve all Customers.
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
        path='/v1/customers.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_json_post(client):
    """Test case for customers_json_post

    Create a new Customer.
    """
    body = {"customer":{"password":"password","phone":"phone","billing_address":{"country":"country","address":"address","city":"city","surname":"surname","taxid":"taxid","municipality":"municipality","name":"name","postal":"postal","region":"region"},"customer_category":[0,0],"shipping_address":{"country":"country","address":"address","city":"city","surname":"surname","municipality":"municipality","name":"name","postal":"postal","region":"region"},"email":"email","status":"approved"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/customers.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

