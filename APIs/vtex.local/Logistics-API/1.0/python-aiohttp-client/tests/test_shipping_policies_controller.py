# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server.models.request_body1 import RequestBody1


pytestmark = pytest.mark.asyncio

async def test_api_logistics_pvt_shipping_policies_get(client):
    """Test case for api_logistics_pvt_shipping_policies_get

    List shipping policies
    """
    params = [('page', 'page'),
                    ('perPage', 'perPage')]
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/shipping-policies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_pvt_shipping_policies_id_delete(client):
    """Test case for api_logistics_pvt_shipping_policies_id_delete

    Delete shipping policies by ID
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/logistics/pvt/shipping-policies/{id}'.format(id='id'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_pvt_shipping_policies_id_get(client):
    """Test case for api_logistics_pvt_shipping_policies_id_get

    Retrieve shipping policy by ID
    """
    headers = { 
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/shipping-policies/{id}'.format(id='id'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_pvt_shipping_policies_id_put(client):
    """Test case for api_logistics_pvt_shipping_policies_id_put

    Update shipping policy
    """
    body = openapi_server.RequestBody1()
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/logistics/pvt/shipping-policies/{id}'.format(id='shippingpolicyid1'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_logistics_pvt_shipping_policies_post(client):
    """Test case for api_logistics_pvt_shipping_policies_post

    Create shipping policy
    """
    body = openapi_server.RequestBody()
    headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/shipping-policies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

