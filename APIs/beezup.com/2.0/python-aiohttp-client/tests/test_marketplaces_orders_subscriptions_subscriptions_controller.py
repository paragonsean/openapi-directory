# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_subscription_request import ActivateSubscriptionRequest
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.create_subscription_request import CreateSubscriptionRequest
from openapi_server.models.error_response_message import ErrorResponseMessage
from openapi_server.models.subscription_index import SubscriptionIndex
from openapi_server.models.subscription_push_reporting import SubscriptionPushReporting


pytestmark = pytest.mark.asyncio

async def test_activate_subscription(client):
    """Test case for activate_subscription

    Activate a subscription to the orders
    """
    body = openapi_server.ActivateSubscriptionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/subscriptions/{id}/activate'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subscription(client):
    """Test case for create_subscription

    Creates a subscription to the orders
    """
    body = openapi_server.CreateSubscriptionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_subscription(client):
    """Test case for deactivate_subscription

    Deactivate a subscription to the orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/subscriptions/{id}/deactivate'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscription(client):
    """Test case for delete_subscription

    Delete a subscription to the orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/user/marketplaces/orders/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    Get a subscription to the orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/subscriptions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_list(client):
    """Test case for get_subscription_list

    Get the subscription list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/subscriptions/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription_push_reporting(client):
    """Test case for get_subscription_push_reporting

    Get the push reporting related to this subscription
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/orders/subscriptions/{id}/reporting'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retry_push_orders(client):
    """Test case for retry_push_orders

    Force retry push orders immediatly
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/orders/subscriptions/{id}/retry'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

