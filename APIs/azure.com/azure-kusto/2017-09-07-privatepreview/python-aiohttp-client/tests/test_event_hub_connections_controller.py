# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.event_hub_connection import EventHubConnection
from openapi_server.models.event_hub_connection_list_result import EventHubConnectionListResult
from openapi_server.models.event_hub_connection_update import EventHubConnectionUpdate
from openapi_server.models.event_hub_connection_validation import EventHubConnectionValidation
from openapi_server.models.event_hub_connection_validation_list_result import EventHubConnectionValidationListResult


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_create_or_update(client):
    """Test case for event_hub_connections_create_or_update

    
    """
    parameters = {"location":"location","properties":{"eventHubResourceId":"eventHubResourceId","dataFormat":"MULTIJSON","mappingRuleName":"mappingRuleName","consumerGroup":"consumerGroup","tableName":"tableName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubconnections/{event_hub_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', event_hub_connection_name='event_hub_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_delete(client):
    """Test case for event_hub_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubconnections/{event_hub_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', event_hub_connection_name='event_hub_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_eventhub_connection_validation(client):
    """Test case for event_hub_connections_eventhub_connection_validation

    
    """
    parameters = {"eventhubConnectionName":"eventhubConnectionName","properties":{"eventHubResourceId":"eventHubResourceId","dataFormat":"MULTIJSON","mappingRuleName":"mappingRuleName","consumerGroup":"consumerGroup","tableName":"tableName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubConnectionValidation'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_get(client):
    """Test case for event_hub_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubconnections/{event_hub_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', event_hub_connection_name='event_hub_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_list_by_database(client):
    """Test case for event_hub_connections_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubconnections'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_event_hub_connections_update(client):
    """Test case for event_hub_connections_update

    
    """
    parameters = {"location":"location","properties":{"eventHubResourceId":"eventHubResourceId","dataFormat":"MULTIJSON","mappingRuleName":"mappingRuleName","consumerGroup":"consumerGroup","tableName":"tableName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Kusto/clusters/{cluster_name}/databases/{database_name}/eventhubconnections/{event_hub_connection_name}'.format(resource_group_name='resource_group_name_example', cluster_name='cluster_name_example', database_name='database_name_example', event_hub_connection_name='event_hub_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

