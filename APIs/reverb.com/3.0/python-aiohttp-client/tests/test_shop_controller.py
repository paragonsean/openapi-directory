# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.shop_put_request import ShopPutRequest


pytestmark = pytest.mark.asyncio

async def test_shop_get(client):
    """Test case for shop_get

    Get your own shop details
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/shop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_listing_conditions_get(client):
    """Test case for shop_listing_conditions_get

    List of supported product conditions
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/shop/listing_conditions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_payment_methods_get(client):
    """Test case for shop_payment_methods_get

    Get accepted payment methods
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/shop/payment_methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_put(client):
    """Test case for shop_put

    Update your shop profile
    """
    body = openapi_server.ShopPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/shop',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_vacation_delete(client):
    """Test case for shop_vacation_delete

    Disable vacation mode. All listings will be re-enabled.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/shop/vacation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_vacation_get(client):
    """Test case for shop_vacation_get

    Returns shop vacation status
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/shop/vacation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shop_vacation_post(client):
    """Test case for shop_vacation_post

    Enable vacation mode. All listings will be unavailable until vacation mode is turned off.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shop/vacation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

