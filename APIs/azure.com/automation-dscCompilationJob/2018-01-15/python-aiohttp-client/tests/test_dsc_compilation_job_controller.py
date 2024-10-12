# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dsc_compilation_job import DscCompilationJob
from openapi_server.models.dsc_compilation_job_create_parameters import DscCompilationJobCreateParameters
from openapi_server.models.dsc_compilation_job_list_by_automation_account_default_response import DscCompilationJobListByAutomationAccountDefaultResponse
from openapi_server.models.dsc_compilation_job_list_result import DscCompilationJobListResult
from openapi_server.models.job_stream import JobStream
from openapi_server.models.job_stream_list_result import JobStreamListResult


pytestmark = pytest.mark.asyncio

async def test_dsc_compilation_job_create(client):
    """Test case for dsc_compilation_job_create

    
    """
    parameters = {"name":"name","location":"location","properties":{"incrementNodeConfigurationBuild":True,"configuration":{"name":"name"},"parameters":{"key":"parameters"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/compilationjobs/{compilation_job_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', compilation_job_name='compilation_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_compilation_job_get(client):
    """Test case for dsc_compilation_job_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/compilationjobs/{compilation_job_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', compilation_job_name='compilation_job_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_compilation_job_get_stream(client):
    """Test case for dsc_compilation_job_get_stream

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/compilationjobs/{job_id}/streams/{job_stream_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_id='job_id_example', job_stream_id='job_stream_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_compilation_job_list_by_automation_account(client):
    """Test case for dsc_compilation_job_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/compilationjobs'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dsc_compilation_job_stream_list_by_job(client):
    """Test case for dsc_compilation_job_stream_list_by_job

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/compilationjobs/{job_id}/streams'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', job_id='job_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

