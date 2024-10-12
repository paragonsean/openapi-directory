# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_version import JobVersion
from openapi_server.models.job_version_list_result import JobVersionListResult


pytestmark = pytest.mark.asyncio

async def test_job_versions_get(client):
    """Test case for job_versions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/versions/{job_version}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', job_version=56, subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_versions_list_by_job(client):
    """Test case for job_versions_list_by_job

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/jobAgents/{job_agent_name}/jobs/{job_name}/versions'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', job_agent_name='job_agent_name_example', job_name='job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

