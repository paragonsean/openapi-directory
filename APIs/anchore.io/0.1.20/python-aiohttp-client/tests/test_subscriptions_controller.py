# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.subscription import Subscription
from openapi_server.models.subscription_request import SubscriptionRequest
from openapi_server.models.subscription_update import SubscriptionUpdate


pytestmark = pytest.mark.asyncio

async def test_add_subscription(client):
    """Test case for add_subscription

    Add a subscription of a specific type
    """
    body = {"subscription_value":"subscription_value","subscription_key":"subscription_key","subscription_type":"subscription_type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_subscription(client):
    """Test case for delete_subscription

    Delete subscriptions of a specific type
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subscription(client):
    """Test case for get_subscription

    Get a specific subscription set
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_subscriptions(client):
    """Test case for list_subscriptions

    List all subscriptions
    """
    params = [('subscription_key', 'subscription_key_example'),
                    ('subscription_type', 'subscription_type_example')]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_subscription(client):
    """Test case for update_subscription

    Update an existing and specific subscription
    """
    body = {"subscription_value":"subscription_value","active":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

