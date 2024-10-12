# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_stream import JobStream
from openapi_server.models.job_stream_list_result import JobStreamListResult
from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_test_job_streams_get(client):
    """Test case for test_job_streams_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob/streams/{job_stream_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example', job_stream_id='job_stream_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_job_streams_list_by_test_job(client):
    """Test case for test_job_streams_list_by_test_job

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob/streams'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

