# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.workload_group import WorkloadGroup
from openapi_server.models.workload_group_list_result import WorkloadGroupListResult


pytestmark = pytest.mark.asyncio

async def test_workload_groups_create_or_update(client):
    """Test case for workload_groups_create_or_update

    
    """
    parameters = {"properties":{"queryExecutionTimeout":5,"maxResourcePercentPerRequest":6.027456183070403,"importance":"importance","minResourcePercentPerRequest":5.962133916683182,"maxResourcePercent":0,"minResourcePercent":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_groups_delete(client):
    """Test case for workload_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_groups_get(client):
    """Test case for workload_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups/{workload_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', workload_group_name='workload_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_workload_groups_list_by_database(client):
    """Test case for workload_groups_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/workloadGroups'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

