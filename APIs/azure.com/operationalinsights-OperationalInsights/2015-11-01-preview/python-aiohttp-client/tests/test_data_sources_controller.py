# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_source import DataSource
from openapi_server.models.data_source_list_result import DataSourceListResult


pytestmark = pytest.mark.asyncio

async def test_data_sources_create_or_update(client):
    """Test case for data_sources_create_or_update

    
    """
    parameters = {"kind":"AzureActivityLog","eTag":"eTag","properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources/{data_source_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', data_source_name='data_source_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sources_delete(client):
    """Test case for data_sources_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources/{data_source_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', data_source_name='data_source_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sources_get(client):
    """Test case for data_sources_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources/{data_source_name}'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', data_source_name='data_source_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_sources_list_by_workspace(client):
    """Test case for data_sources_list_by_workspace

    
    """
    params = [('$filter', 'filter_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/dataSources'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

