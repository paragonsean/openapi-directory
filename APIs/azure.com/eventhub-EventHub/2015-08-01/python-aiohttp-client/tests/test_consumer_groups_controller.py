# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.consumer_group_create_or_update_parameters import ConsumerGroupCreateOrUpdateParameters
from openapi_server.models.consumer_group_list_result import ConsumerGroupListResult
from openapi_server.models.consumer_group_resource import ConsumerGroupResource


pytestmark = pytest.mark.asyncio

async def test_consumer_groups_create_or_update(client):
    """Test case for consumer_groups_create_or_update

    
    """
    parameters = {"name":"name","location":"location","type":"type","properties":{"createdAt":"2000-01-23T04:56:07.000+00:00","eventHubPath":"eventHubPath","userMetadata":"userMetadata","updatedAt":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventHub/namespaces/{namespace_name}/eventhubs/{event_hub_name}/consumergroups/{consumer_group_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', event_hub_name='event_hub_name_example', consumer_group_name='consumer_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_groups_delete(client):
    """Test case for consumer_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventHub/namespaces/{namespace_name}/eventhubs/{event_hub_name}/consumergroups/{consumer_group_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', event_hub_name='event_hub_name_example', consumer_group_name='consumer_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_groups_get(client):
    """Test case for consumer_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventHub/namespaces/{namespace_name}/eventhubs/{event_hub_name}/consumergroups/{consumer_group_name}'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', event_hub_name='event_hub_name_example', consumer_group_name='consumer_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consumer_groups_list_all(client):
    """Test case for consumer_groups_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EventHub/namespaces/{namespace_name}/eventhubs/{event_hub_name}/consumergroups'.format(resource_group_name='resource_group_name_example', namespace_name='namespace_name_example', event_hub_name='event_hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

