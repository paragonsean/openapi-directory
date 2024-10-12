# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.storage_insight import StorageInsight
from openapi_server.models.storage_insight_list_result import StorageInsightListResult


pytestmark = pytest.mark.asyncio

async def test_storage_insights_create_or_update(client):
    """Test case for storage_insights_create_or_update

    
    """
    parameters = {"eTag":"eTag","properties":{"tables":["tables","tables"],"containers":["containers","containers"],"storageAccount":{"id":"id","key":"key"},"status":{"description":"description","state":"OK"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/storageInsightConfigs/{storage_insight_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', storage_insight_name='storage_insight_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_insights_delete(client):
    """Test case for storage_insights_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/storageInsightConfigs/{storage_insight_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', storage_insight_name='storage_insight_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_insights_get(client):
    """Test case for storage_insights_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/storageInsightConfigs/{storage_insight_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', storage_insight_name='storage_insight_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_insights_list_by_workspace(client):
    """Test case for storage_insights_list_by_workspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/storageInsightConfigs'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

