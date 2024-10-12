# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.keys_api_find200_response import KeysApiFind200Response
from openapi_server.models.products_api_count200_response import ProductsApiCount200Response
from openapi_server.models.products_api_find_request import ProductsApiFindRequest
from openapi_server.models.subscription_view import SubscriptionView
from openapi_server.models.subscriptions_api_count_request import SubscriptionsApiCountRequest
from openapi_server.models.subscriptions_api_find200_response import SubscriptionsApiFind200Response
from openapi_server.models.subscriptions_api_put_subscription_request import SubscriptionsApiPutSubscriptionRequest


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_count(client):
    """Test case for subscriptions_api_count

    
    """
    body = openapi_server.SubscriptionsApiCountRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/Count',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_delete_subscription(client):
    """Test case for subscriptions_api_delete_subscription

    
    """
    params = [('keep', True)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/SubscriptionsApi/{serial}'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_delete_subscription2(client):
    """Test case for subscriptions_api_delete_subscription2

    
    """
    params = [('keep', True)]
    headers = { 
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/{serial}'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_disable(client):
    """Test case for subscriptions_api_disable

    
    """
    body = openapi_server.ProductsApiFindRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/SubscriptionsApi/Disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_disable2(client):
    """Test case for subscriptions_api_disable2

    
    """
    body = openapi_server.ProductsApiFindRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/Disable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_enable(client):
    """Test case for subscriptions_api_enable

    
    """
    body = openapi_server.ProductsApiFindRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/SubscriptionsApi/Enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_enable2(client):
    """Test case for subscriptions_api_enable2

    
    """
    body = openapi_server.ProductsApiFindRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/Enable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_find(client):
    """Test case for subscriptions_api_find

    
    """
    body = openapi_server.ProductsApiFindRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/Find',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_list(client):
    """Test case for subscriptions_api_list

    
    """
    body = openapi_server.ProductsApiFindRequest()
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/List',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_put_subscription(client):
    """Test case for subscriptions_api_put_subscription

    
    """
    body = openapi_server.SubscriptionsApiPutSubscriptionRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/SubscriptionsApi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_put_subscription2(client):
    """Test case for subscriptions_api_put_subscription2

    
    """
    body = openapi_server.SubscriptionsApiPutSubscriptionRequest()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_api_save(client):
    """Test case for subscriptions_api_save

    
    """
    body = openapi_server.SubscriptionsApiPutSubscriptionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/SubscriptionsApi/Save',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

