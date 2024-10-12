# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_execution import JobExecution
from openapi_server.models.job_execution_list_result import JobExecutionListResult


pytestmark = pytest.mark.asyncio

async def test_job_target_executions_get(client):
    """Test case for job_target_executions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}/steps/{step_name}/targets/{target_id}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', step_name='step_name_example', target_id='target_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_target_executions_list_by_job_execution(client):
    """Test case for job_target_executions_list_by_job_execution

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}/targets'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_target_executions_list_by_step(client):
    """Test case for job_target_executions_list_by_step

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/executions/{job_execution_id}/steps/{step_name}/targets'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_execution_id='job_execution_id_example', step_name='step_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

