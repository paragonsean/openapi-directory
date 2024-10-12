# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_target_group import JobTargetGroup
from openapi_server.models.job_target_group_list_result import JobTargetGroupListResult


pytestmark = pytest.mark.asyncio

async def test_job_target_groups_create_or_update(client):
    """Test case for job_target_groups_create_or_update

    
    """
    parameters = {"properties":{"members":[{"membershipType":"Include","elasticPoolName":"elasticPoolName","databaseName":"databaseName","shardMapName":"shardMapName","serverName":"serverName","refreshCredential":"refreshCredential","type":"TargetGroup"},{"membershipType":"Include","elasticPoolName":"elasticPoolName","databaseName":"databaseName","shardMapName":"shardMapName","serverName":"serverName","refreshCredential":"refreshCredential","type":"TargetGroup"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/targetGroups/{target_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', target_group_name='target_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_target_groups_delete(client):
    """Test case for job_target_groups_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/targetGroups/{target_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', target_group_name='target_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_target_groups_get(client):
    """Test case for job_target_groups_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/targetGroups/{target_group_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', target_group_name='target_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_target_groups_list_by_agent(client):
    """Test case for job_target_groups_list_by_agent

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/targetGroups'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

