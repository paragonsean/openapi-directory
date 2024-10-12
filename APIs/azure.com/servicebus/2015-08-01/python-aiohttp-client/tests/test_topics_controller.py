# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.regenerate_keys_parameters import RegenerateKeysParameters
from openapi_server.models.resource_list_keys import ResourceListKeys
from openapi_server.models.shared_access_authorization_rule_create_or_update_parameters import SharedAccessAuthorizationRuleCreateOrUpdateParameters
from openapi_server.models.shared_access_authorization_rule_list_result import SharedAccessAuthorizationRuleListResult
from openapi_server.models.shared_access_authorization_rule_resource import SharedAccessAuthorizationRuleResource
from openapi_server.models.topic_create_or_update_parameters import TopicCreateOrUpdateParameters
from openapi_server.models.topic_list_result import TopicListResult
from openapi_server.models.topic_resource import TopicResource


pytestmark = pytest.mark.asyncio

async def test_topics_create_or_update(client):
    """Test case for topics_create_or_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"accessedAt":"2000-01-23T04:56:07.000+00:00","sizeInBytes":6,"enablePartitioning":True,"supportOrdering":True,"subscriptionCount":1,"entityAvailabilityStatus":"Available","isExpress":True,"createdAt":"2000-01-23T04:56:07.000+00:00","autoDeleteOnIdle":"autoDeleteOnIdle","filteringMessagesBeforePublishing":True,"enableBatchedOperations":True,"enableExpress":True,"isAnonymousAccessible":True,"maxSizeInMegabytes":0,"countDetails":{"scheduledMessageCount":1,"transferMessageCount":5,"transferDeadLetterMessageCount":5,"deadLetterMessageCount":6,"activeMessageCount":0},"duplicateDetectionHistoryTimeWindow":"duplicateDetectionHistoryTimeWindow","requiresDuplicateDetection":True,"defaultMessageTimeToLive":"defaultMessageTimeToLive","status":"Active","updatedAt":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_create_or_update_authorization_rule(client):
    """Test case for topics_create_or_update_authorization_rule

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_delete(client):
    """Test case for topics_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_delete_authorization_rule(client):
    """Test case for topics_delete_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_get(client):
    """Test case for topics_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_get_authorization_rule(client):
    """Test case for topics_get_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_all(client):
    """Test case for topics_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_authorization_rules(client):
    """Test case for topics_list_authorization_rules

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_keys(client):
    """Test case for topics_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}/ListKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_post_authorization_rule(client):
    """Test case for topics_post_authorization_rule

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_regenerate_keys(client):
    """Test case for topics_regenerate_keys

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceBus/namespaces/{namespace_name}/topics/{topic_name}/authorizationRules/{authorization_rule_name}/regenerateKeys'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', topic_name='topic_name_example', authorization_rule_name='authorization_rule_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

