# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.source_control_sync_job import SourceControlSyncJob
from openapi_server.models.source_control_sync_job_by_id import SourceControlSyncJobById
from openapi_server.models.source_control_sync_job_create_parameters import SourceControlSyncJobCreateParameters
from openapi_server.models.source_control_sync_job_list_by_automation_account_default_response import SourceControlSyncJobListByAutomationAccountDefaultResponse
from openapi_server.models.source_control_sync_job_list_result import SourceControlSyncJobListResult


pytestmark = pytest.mark.asyncio

async def test_source_control_sync_job_create(client):
    """Test case for source_control_sync_job_create

    
    """
    parameters = {"properties":{"commitId":"commitId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}/sourceControlSyncJobs/{source_control_sync_job_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', source_control_sync_job_id='source_control_sync_job_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_sync_job_get(client):
    """Test case for source_control_sync_job_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}/sourceControlSyncJobs/{source_control_sync_job_id}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', source_control_sync_job_id='source_control_sync_job_id_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_sync_job_list_by_automation_account(client):
    """Test case for source_control_sync_job_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}/sourceControlSyncJobs'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

