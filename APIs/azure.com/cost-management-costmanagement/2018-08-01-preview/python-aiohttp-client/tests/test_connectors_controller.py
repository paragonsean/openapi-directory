# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connector_definition import ConnectorDefinition
from openapi_server.models.connector_definition_list_result import ConnectorDefinitionListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_connector_create_or_update(client):
    """Test case for connector_create_or_update

    
    """
    connector = {"kind":"kind","name":"name","location":"location","id":"id","type":"type","properties":{"modifiedOn":"2000-01-23T04:56:07.000+00:00","reportId":"reportId","credentialsSecret":"credentialsSecret","displayName":"displayName","providerAccountId":"providerAccountId","collection":{"lastUpdated":"2000-01-23T04:56:07.000+00:00","sourceLastUpdated":"2000-01-23T04:56:07.000+00:00","lastRun":"2000-01-23T04:56:07.000+00:00","error":{"errorMessage":"errorMessage","errorCode":"errorCode","errorStartTime":"2000-01-23T04:56:07.000+00:00"}},"credentialsKey":"credentialsKey","createdOn":"2000-01-23T04:56:07.000+00:00","status":"active"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/connectors/{connector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connector_name='connector_name_example'),
        headers=headers,
        json=connector,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_delete(client):
    """Test case for connector_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/connectors/{connector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connector_name='connector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_get(client):
    """Test case for connector_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/connectors/{connector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connector_name='connector_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_list(client):
    """Test case for connector_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.CostManagement/connectors'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_list_by_resource_group_name(client):
    """Test case for connector_list_by_resource_group_name

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/connectors'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_update(client):
    """Test case for connector_update

    
    """
    connector = {"kind":"kind","name":"name","location":"location","id":"id","type":"type","properties":{"modifiedOn":"2000-01-23T04:56:07.000+00:00","reportId":"reportId","credentialsSecret":"credentialsSecret","displayName":"displayName","providerAccountId":"providerAccountId","collection":{"lastUpdated":"2000-01-23T04:56:07.000+00:00","sourceLastUpdated":"2000-01-23T04:56:07.000+00:00","lastRun":"2000-01-23T04:56:07.000+00:00","error":{"errorMessage":"errorMessage","errorCode":"errorCode","errorStartTime":"2000-01-23T04:56:07.000+00:00"}},"credentialsKey":"credentialsKey","createdOn":"2000-01-23T04:56:07.000+00:00","status":"active"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.CostManagement/connectors/{connector_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', connector_name='connector_name_example'),
        headers=headers,
        json=connector,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

