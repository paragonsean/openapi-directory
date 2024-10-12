# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_input_subscription_batch_update_request import BatchInputSubscriptionBatchUpdateRequest
from openapi_server.models.batch_response_subscription_response import BatchResponseSubscriptionResponse
from openapi_server.models.batch_response_subscription_response_with_errors import BatchResponseSubscriptionResponseWithErrors
from openapi_server.models.error import Error
from openapi_server.models.subscription_create_request import SubscriptionCreateRequest
from openapi_server.models.subscription_list_response import SubscriptionListResponse
from openapi_server.models.subscription_patch_request import SubscriptionPatchRequest
from openapi_server.models.subscription_response import SubscriptionResponse


pytestmark = pytest.mark.asyncio

async def test_delete_webhooks_v3_app_id_subscriptions_subscription_id_archive(client):
    """Test case for delete_webhooks_v3_app_id_subscriptions_subscription_id_archive

    
    """
    headers = { 
        'Accept': '*/*',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/webhooks/v3/{app_id}/subscriptions/{subscription_id}'.format(subscription_id=56, app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhooks_v3_app_id_subscriptions_get_all(client):
    """Test case for get_webhooks_v3_app_id_subscriptions_get_all

    
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhooks/v3/{app_id}/subscriptions'.format(app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhooks_v3_app_id_subscriptions_subscription_id_get_by_id(client):
    """Test case for get_webhooks_v3_app_id_subscriptions_subscription_id_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/webhooks/v3/{app_id}/subscriptions/{subscription_id}'.format(subscription_id=56, app_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_webhooks_v3_app_id_subscriptions_subscription_id_update(client):
    """Test case for patch_webhooks_v3_app_id_subscriptions_subscription_id_update

    
    """
    body = {"active":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/webhooks/v3/{app_id}/subscriptions/{subscription_id}'.format(subscription_id=56, app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_webhooks_v3_app_id_subscriptions_batch_update_update_batch(client):
    """Test case for post_webhooks_v3_app_id_subscriptions_batch_update_update_batch

    
    """
    body = {"inputs":[{"active":True,"id":0},{"active":True,"id":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/webhooks/v3/{app_id}/subscriptions/batch/update'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_webhooks_v3_app_id_subscriptions_create(client):
    """Test case for post_webhooks_v3_app_id_subscriptions_create

    
    """
    body = {"active":True,"eventType":"contact.propertyChange","propertyName":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'developer_hapikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/webhooks/v3/{app_id}/subscriptions'.format(app_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

