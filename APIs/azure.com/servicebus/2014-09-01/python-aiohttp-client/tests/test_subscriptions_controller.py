# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_create_or_update_parameters import SubscriptionCreateOrUpdateParameters
from openapi_server.models.subscription_list_result import SubscriptionListResult
from openapi_server.models.subscription_resource import SubscriptionResource


pytestmark = pytest.mark.asyncio

async def test_subscriptions_create_or_update(client):
    """Test case for subscriptions_create_or_update

    
    """
    parameters = {"location":"location","type":"type","properties":{"accessedAt":"2000-01-23T04:56:07.000+00:00","deadLetteringOnFilterEvaluationExceptions":True,"messageCount":6,"lockDuration":"lockDuration","requiresSession":True,"deadLetteringOnMessageExpiration":True,"entityAvailabilityStatus":"Available","maxDeliveryCount":0,"createdAt":"2000-01-23T04:56:07.000+00:00","autoDeleteOnIdle":"autoDeleteOnIdle","isReadOnly":True,"enableBatchedOperations":True,"countDetails":{"scheduledMessageCount":1,"transferMessageCount":5,"transferDeadLetterMessageCount":5,"deadLetterMessageCount":6,"activeMessageCount":0},"defaultMessageTimeToLive":"defaultMessageTimeToLive","status":"Active","updatedAt":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_delete(client):
    """Test case for subscriptions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_get(client):
    """Test case for subscriptions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions/{subscription_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_name='subscription_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subscriptions_list_all(client):
    """Test case for subscriptions_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/subscriptions'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

