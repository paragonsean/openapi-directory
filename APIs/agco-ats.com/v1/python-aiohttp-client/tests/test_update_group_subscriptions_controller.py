# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_update_system_models_update_group_subscription import APIPagedResponseUpdateSystemModelsUpdateGroupSubscription
from openapi_server.models.update_system_models_update_group_subscription import UpdateSystemModelsUpdateGroupSubscription


pytestmark = pytest.mark.asyncio

async def test_update_group_subscriptions_delete_update_group_subscription(client):
    """Test case for update_group_subscriptions_delete_update_group_subscription

    Delete an Update Group Subscription
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/UpdateGroupSubscriptions/{update_group_subscription_id}'.format(update_group_subscription_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_subscriptions_get_update_group_subscription(client):
    """Test case for update_group_subscriptions_get_update_group_subscription

    Get an Update Group Subscription
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroupSubscriptions/{update_group_subscription_id}'.format(update_group_subscription_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_group_subscriptions_get_update_group_subscriptions(client):
    """Test case for update_group_subscriptions_get_update_group_subscriptions

    Get Update Group Subscriptions
    """
    params = [('UpdateGroupID', 'update_group_id_example'),
                    ('PackageTypeID', 'package_type_id_example'),
                    ('ClientID', 'client_id_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/UpdateGroupSubscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_subscriptions_post_update_group_subscription(client):
    """Test case for update_group_subscriptions_post_update_group_subscription

    Add an Update Group Subscription
    """
    body = openapi_server.UpdateSystemModelsUpdateGroupSubscription()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UpdateGroupSubscriptions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_subscriptions_post_update_group_subscriptions(client):
    """Test case for update_group_subscriptions_post_update_group_subscriptions

    No Documentation Found.
    """
    body = [openapi_server.UpdateSystemModelsUpdateGroupSubscription()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/UpdateGroupSubscriptions/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_subscriptions_put_update_group_subscription(client):
    """Test case for update_group_subscriptions_put_update_group_subscription

    Update an Update Group Subscription
    """
    body = openapi_server.UpdateSystemModelsUpdateGroupSubscription()
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/UpdateGroupSubscriptions/{update_group_subscription_id}'.format(update_group_subscription_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_group_subscriptions_put_update_group_subscriptions(client):
    """Test case for update_group_subscriptions_put_update_group_subscriptions

    No Documentation Found.
    """
    body = [openapi_server.UpdateSystemModelsUpdateGroupSubscription()]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/UpdateGroupSubscriptions/Batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

