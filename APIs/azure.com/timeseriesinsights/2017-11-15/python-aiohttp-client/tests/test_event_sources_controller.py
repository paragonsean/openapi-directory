# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.event_source_create_or_update_parameters import EventSourceCreateOrUpdateParameters
from openapi_server.models.event_source_list_response import EventSourceListResponse
from openapi_server.models.event_source_resource import EventSourceResource
from openapi_server.models.event_source_update_parameters import EventSourceUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_event_sources_create_or_update(client):
    """Test case for event_sources_create_or_update

    
    """
    parameters = {"kind":"Microsoft.EventHub"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/eventSources/{event_source_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', event_source_name='event_source_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_sources_delete(client):
    """Test case for event_sources_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/eventSources/{event_source_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', event_source_name='event_source_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_sources_get(client):
    """Test case for event_sources_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/eventSources/{event_source_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', event_source_name='event_source_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_sources_list_by_environment(client):
    """Test case for event_sources_list_by_environment

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/eventSources'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_sources_update(client):
    """Test case for event_sources_update

    
    """
    event_source_update_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.TimeSeriesInsights/environments/{environment_name}/eventSources/{event_source_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', environment_name='environment_name_example', event_source_name='event_source_name_example'),
        headers=headers,
        json=event_source_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

