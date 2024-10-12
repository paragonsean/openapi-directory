# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_cart_item_input import AddCartItemInput
from openapi_server.models.remote_shopcart_response import RemoteShopcartResponse
from openapi_server.models.remove_cart_item_input import RemoveCartItemInput
from openapi_server.models.update_cart_item_input import UpdateCartItemInput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_item(client):
    """Test case for add_item

    
    """
    body = openapi_server.AddCartItemInput()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buy/browse/v1/shopping_cart/add_item',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shopping_cart(client):
    """Test case for get_shopping_cart

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/buy/browse/v1/shopping_cart/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remove_item(client):
    """Test case for remove_item

    
    """
    body = openapi_server.RemoveCartItemInput()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buy/browse/v1/shopping_cart/remove_item',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_quantity(client):
    """Test case for update_quantity

    
    """
    body = openapi_server.UpdateCartItemInput()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/buy/browse/v1/shopping_cart/update_quantity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

