# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_list_by_automation_account_default_response import JobListByAutomationAccountDefaultResponse
from openapi_server.models.job_stream import JobStream
from openapi_server.models.job_stream_list_result import JobStreamListResult


pytestmark = pytest.mark.asyncio

async def test_job_stream_get(client):
    """Test case for job_stream_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_id}/streams/{job_stream_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_id='job_id_example', job_stream_id='job_stream_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_stream_list_by_job(client):
    """Test case for job_stream_list_by_job

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_id}/streams'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_id='job_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

