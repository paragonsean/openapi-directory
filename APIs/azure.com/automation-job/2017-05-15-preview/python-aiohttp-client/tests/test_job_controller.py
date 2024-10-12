# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.job_create_parameters import JobCreateParameters
from openapi_server.models.job_list_by_automation_account_default_response import JobListByAutomationAccountDefaultResponse
from openapi_server.models.job_list_result_v2 import JobListResultV2


pytestmark = pytest.mark.asyncio

async def test_job_create(client):
    """Test case for job_create

    
    """
    parameters = {"properties":{"runOn":"runOn","parameters":{"key":"parameters"},"runbook":{"name":"name"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get(client):
    """Test case for job_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_output(client):
    """Test case for job_get_output

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'text/plain',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}/output'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_get_runbook_content(client):
    """Test case for job_get_runbook_content

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}/runbookContent'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_list_by_automation_account(client):
    """Test case for job_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_resume(client):
    """Test case for job_resume

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}/resume'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_stop(client):
    """Test case for job_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}/stop'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_suspend(client):
    """Test case for job_suspend

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'client_request_id': 'client_request_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/jobs/{job_name}/suspend'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

