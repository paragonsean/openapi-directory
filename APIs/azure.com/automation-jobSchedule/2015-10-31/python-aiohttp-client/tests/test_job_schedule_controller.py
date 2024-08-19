# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_schedule import JobSchedule
from openapi_server.models.job_schedule_create_parameters import JobScheduleCreateParameters
from openapi_server.models.job_schedule_list_by_automation_account_default_response import JobScheduleListByAutomationAccountDefaultResponse
from openapi_server.models.job_schedule_list_result import JobScheduleListResult


pytestmark = pytest.mark.asyncio

async def test_job_schedule_create(client):
    """Test case for job_schedule_create

    
    """
    parameters = {"properties":{"schedule":{"name":"name"},"runOn":"runOn","parameters":{"key":"parameters"},"runbook":{"name":"name"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobSchedules/{job_schedule_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_schedule_id='job_schedule_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_schedule_delete(client):
    """Test case for job_schedule_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobSchedules/{job_schedule_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_schedule_id='job_schedule_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_schedule_get(client):
    """Test case for job_schedule_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobSchedules/{job_schedule_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_schedule_id='job_schedule_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_schedule_list_by_automation_account(client):
    """Test case for job_schedule_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobSchedules'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

