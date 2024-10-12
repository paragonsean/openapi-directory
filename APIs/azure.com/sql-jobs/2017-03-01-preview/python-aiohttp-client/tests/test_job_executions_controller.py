# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_execution import JobExecution
from openapi_server.models.job_execution_list_result import JobExecutionListResult


pytestmark = pytest.mark.asyncio

async def test_job_executions_cancel(client):
    """Test case for job_executions_cancel

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}/cancel'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_executions_create(client):
    """Test case for job_executions_create

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/start'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_executions_create_or_update(client):
    """Test case for job_executions_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_executions_get(client):
    """Test case for job_executions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_executions_list_by_agent(client):
    """Test case for job_executions_list_by_agent

    
    """
    params = [('createTimeMin', '2013-10-20T19:20:30+01:00'),
                    ('createTimeMax', '2013-10-20T19:20:30+01:00'),
                    ('endTimeMin', '2013-10-20T19:20:30+01:00'),
                    ('endTimeMax', '2013-10-20T19:20:30+01:00'),
                    ('isActive', True),
                    ('$skip', 56),
                    ('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/executions'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_executions_list_by_job(client):
    """Test case for job_executions_list_by_job

    
    """
    params = [('createTimeMin', '2013-10-20T19:20:30+01:00'),
                    ('createTimeMax', '2013-10-20T19:20:30+01:00'),
                    ('endTimeMin', '2013-10-20T19:20:30+01:00'),
                    ('endTimeMax', '2013-10-20T19:20:30+01:00'),
                    ('isActive', True),
                    ('$skip', 56),
                    ('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

