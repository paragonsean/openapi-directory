# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.shipping_method import ShippingMethod
from openapi_server.models.shipping_method_edit import ShippingMethodEdit


pytestmark = pytest.mark.asyncio

async def test_shipping_methods_id_json_delete(client):
    """Test case for shipping_methods_id_json_delete

    Delete an existing Shipping Method.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/shipping_methods/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipping_methods_id_json_get(client):
    """Test case for shipping_methods_id_json_get

    Retrieve a single Shipping Method.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipping_methods/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipping_methods_id_json_put(client):
    """Test case for shipping_methods_id_json_put

    Update a Shipping Method.
    """
    body = {"shipping_method":{"callback_url":"callback_url","fetch_services_url":"fetch_services_url","city":"city","name":"name","postal":"postal","state":"state","token":"token"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/shipping_methods/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipping_methods_json_get(client):
    """Test case for shipping_methods_json_get

    Retrieve all Store's Shipping Methods.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/shipping_methods.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shipping_methods_json_post(client):
    """Test case for shipping_methods_json_post

    Creates a Shipping Method.
    """
    body = {"shipping_method":{"callback_url":"callback_url","fetch_services_url":"fetch_services_url","city":"city","name":"name","postal":"postal","state":"state","token":"token"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/shipping_methods.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

