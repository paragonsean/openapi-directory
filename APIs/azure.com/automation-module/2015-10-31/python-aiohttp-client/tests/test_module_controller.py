# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.module import Module
from openapi_server.models.module_create_or_update_parameters import ModuleCreateOrUpdateParameters
from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse
from openapi_server.models.module_list_result import ModuleListResult
from openapi_server.models.module_update_parameters import ModuleUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_module_create_or_update(client):
    """Test case for module_create_or_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"contentLink":{"uri":"uri","version":"version","contentHash":{"value":"value","algorithm":"algorithm"}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_module_delete(client):
    """Test case for module_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_module_get(client):
    """Test case for module_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_module_list_by_automation_account(client):
    """Test case for module_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_module_update(client):
    """Test case for module_update

    
    """
    parameters = {"name":"name","location":"location","properties":{"contentLink":{"uri":"uri","version":"version","contentHash":{"value":"value","algorithm":"algorithm"}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

