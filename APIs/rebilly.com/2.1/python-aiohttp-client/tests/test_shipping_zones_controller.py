# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.invalid_error import InvalidError
from openapi_server.models.shipping_zone import ShippingZone


pytestmark = pytest.mark.asyncio

async def test_delete_shipping_zone(client):
    """Test case for delete_shipping_zone

    Delete a shipping zone
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/shipping-zones/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipping_zone(client):
    """Test case for get_shipping_zone

    Retrieve a shipping zone
    """
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/shipping-zones/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shipping_zone_collection(client):
    """Test case for get_shipping_zone_collection

    Retrieve a list of shipping zones
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('filter', 'filter_example'),
                    ('sort', ['sort_example']),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/shipping-zones',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_shipping_zone(client):
    """Test case for post_shipping_zone

    Create a Shipping Zone
    """
    body = {"updatedTime":"","isDefault":"","_links":[{"rel":"self"},{"rel":"self"}],"rates":["",""],"name":"name","createdTime":"","countries":["countries","countries"],"id":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/shipping-zones',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_shipping_zone(client):
    """Test case for put_shipping_zone

    Create a shipping zone with predefined ID
    """
    body = {"updatedTime":"","isDefault":"","_links":[{"rel":"self"},{"rel":"self"}],"rates":["",""],"name":"name","createdTime":"","countries":["countries","countries"],"id":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'organization_id': 'organization_id_example',
        'SecretApiKey': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/shipping-zones/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

