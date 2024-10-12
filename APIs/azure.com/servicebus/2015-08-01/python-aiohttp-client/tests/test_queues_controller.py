# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.queue_create_or_update_parameters import QueueCreateOrUpdateParameters
from openapi_server.models.queue_list_result import QueueListResult
from openapi_server.models.queue_resource import QueueResource
from openapi_server.models.regenerate_keys_parameters import RegenerateKeysParameters
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource


pytestmark = pytest.mark.asyncio

async def test_queues_create_or_update(client):
    """Test case for queues_create_or_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"accessedAt":"2000-01-23T04:56:07.000+00:00","messageCount":9,"sizeInBytes":3,"lockDuration":"lockDuration","enablePartitioning":True,"requiresSession":True,"supportOrdering":True,"deadLetteringOnMessageExpiration":True,"entityAvailabilityStatus":"Available","maxDeliveryCount":2,"createdAt":"2000-01-23T04:56:07.000+00:00","autoDeleteOnIdle":"autoDeleteOnIdle","enableBatchedOperations":True,"enableExpress":True,"isAnonymousAccessible":True,"maxSizeInMegabytes":7,"countDetails":{"scheduledMessageCount":1,"transferMessageCount":5,"transferDeadLetterMessageCount":5,"deadLetterMessageCount":6,"activeMessageCount":0},"duplicateDetectionHistoryTimeWindow":"duplicateDetectionHistoryTimeWindow","requiresDuplicateDetection":True,"defaultMessageTimeToLive":"defaultMessageTimeToLive","status":"Active","updatedAt":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_create_or_update_authorization_rule(client):
    """Test case for queues_create_or_update_authorization_rule

    
    """
    parameters = {"name":"name","location":"location","properties":{"rights":["Manage","Manage"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_delete(client):
    """Test case for queues_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_delete_authorization_rule(client):
    """Test case for queues_delete_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_get(client):
    """Test case for queues_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_get_authorization_rule(client):
    """Test case for queues_get_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_list_all(client):
    """Test case for queues_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_list_authorization_rules(client):
    """Test case for queues_list_authorization_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_list_keys(client):
    """Test case for queues_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}/ListKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_post_authorization_rule(client):
    """Test case for queues_post_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queues_regenerate_keys(client):
    """Test case for queues_regenerate_keys

    
    """
    parameters = {"Policykey":"PrimaryKey"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/queues/{queue_name}/authorizationRules/{authorization_rule_name}/regenerateKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', queue_name='queue_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

