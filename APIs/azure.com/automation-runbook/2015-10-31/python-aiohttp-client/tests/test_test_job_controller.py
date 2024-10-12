# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.runbook_list_by_automation_account_default_response import RunbookListByAutomationAccountDefaultResponse
from openapi_server.models.test_job import TestJob
from openapi_server.models.test_job_create_parameters import TestJobCreateParameters


pytestmark = pytest.mark.asyncio

async def test_test_job_create(client):
    """Test case for test_job_create

    
    """
    parameters = {"runOn":"runOn","parameters":{"key":"parameters"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_job_get(client):
    """Test case for test_job_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_job_resume(client):
    """Test case for test_job_resume

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob/resume'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_job_stop(client):
    """Test case for test_job_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_job_suspend(client):
    """Test case for test_job_suspend

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/runbooks/{runbook_name}/draft/testJob/suspend'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', runbook_name='runbook_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

