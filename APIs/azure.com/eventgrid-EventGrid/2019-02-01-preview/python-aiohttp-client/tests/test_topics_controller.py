# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_types_list_result import EventTypesListResult
from openapi_server.models.topic import Topic
from openapi_server.models.topic_regenerate_key_request import TopicRegenerateKeyRequest
from openapi_server.models.topic_shared_access_keys import TopicSharedAccessKeys
from openapi_server.models.topic_update_parameters import TopicUpdateParameters
from openapi_server.models.topics_list_result import TopicsListResult


pytestmark = pytest.mark.asyncio

async def test_topics_create_or_update(client):
    """Test case for topics_create_or_update

    Create a topic
    """
    topic_info = {"properties":{"endpoint":"endpoint","inputSchema":"EventGridSchema","inputSchemaMapping":{"inputSchemaMappingType":"Json"},"provisioningState":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        json=topic_info,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_delete(client):
    """Test case for topics_delete

    Delete a topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_get(client):
    """Test case for topics_get

    Get a topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_by_resource_group(client):
    """Test case for topics_list_by_resource_group

    List topics under a resource group
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_by_subscription(client):
    """Test case for topics_list_by_subscription

    List topics under an Azure subscription
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.EventGrid/topics'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_event_types(client):
    """Test case for topics_list_event_types

    List topic event types
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/{provider_namespace}/{resource_type_name}/{resource_name}/providers/Microsoft.EventGrid/eventTypes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provider_namespace='provider_namespace_example', resource_type_name='resource_type_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_list_shared_access_keys(client):
    """Test case for topics_list_shared_access_keys

    List keys for a topic
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}/listKeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_regenerate_key(client):
    """Test case for topics_regenerate_key

    Regenerate key for a topic
    """
    regenerate_key_request = {"keyName":"keyName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}/regenerateKey'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        json=regenerate_key_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_topics_update(client):
    """Test case for topics_update

    Update a topic
    """
    topic_update_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventGrid/topics/{topic_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', topic_name='topic_name_example'),
        headers=headers,
        json=topic_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

