# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.source_control import SourceControl
from openapi_server.models.source_control_create_or_update_parameters import SourceControlCreateOrUpdateParameters
from openapi_server.models.source_control_list_by_automation_account_default_response import SourceControlListByAutomationAccountDefaultResponse
from openapi_server.models.source_control_list_result import SourceControlListResult
from openapi_server.models.source_control_update_parameters import SourceControlUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_source_control_create_or_update(client):
    """Test case for source_control_create_or_update

    
    """
    parameters = {"properties":{"folderPath":"folderPath","repoUrl":"repoUrl","securityToken":{"accessToken":"accessToken","tokenType":"PersonalAccessToken","refreshToken":"refreshToken"},"publishRunbook":True,"sourceType":"VsoGit","description":"description","autoSync":True,"branch":"branch"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_delete(client):
    """Test case for source_control_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_get(client):
    """Test case for source_control_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_list_by_automation_account(client):
    """Test case for source_control_list_by_automation_account

    
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_source_control_update(client):
    """Test case for source_control_update

    
    """
    parameters = {"properties":{"folderPath":"folderPath","securityToken":{"accessToken":"accessToken","tokenType":"PersonalAccessToken","refreshToken":"refreshToken"},"publishRunbook":True,"description":"description","autoSync":True,"branch":"branch"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/sourceControls/{source_control_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', source_control_name='source_control_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

