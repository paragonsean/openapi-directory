# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_agent import JobAgent
from openapi_server.models.job_agent_list_result import JobAgentListResult
from openapi_server.models.job_agent_update import JobAgentUpdate


pytestmark = pytest.mark.asyncio

async def test_job_agents_create_or_update(client):
    """Test case for job_agents_create_or_update

    
    """
    parameters = {"sku":"{}","properties":{"state":"Creating","databaseId":"databaseId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_agents_delete(client):
    """Test case for job_agents_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_agents_get(client):
    """Test case for job_agents_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_agents_list_by_server(client):
    """Test case for job_agents_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_agents_update(client):
    """Test case for job_agents_update

    
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

