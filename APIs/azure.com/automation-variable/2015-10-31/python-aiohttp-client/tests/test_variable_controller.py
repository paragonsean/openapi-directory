# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.variable import Variable
from openapi_server.models.variable_create_or_update_parameters import VariableCreateOrUpdateParameters
from openapi_server.models.variable_list_by_automation_account_default_response import VariableListByAutomationAccountDefaultResponse
from openapi_server.models.variable_list_result import VariableListResult
from openapi_server.models.variable_update_parameters import VariableUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_variable_create_or_update(client):
    """Test case for variable_create_or_update

    
    """
    parameters = {"name":"name","properties":{"isEncrypted":True,"description":"description","value":"value"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/variables/{variable_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', variable_name='variable_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_variable_delete(client):
    """Test case for variable_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/variables/{variable_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', variable_name='variable_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_variable_get(client):
    """Test case for variable_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/variables/{variable_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', variable_name='variable_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_variable_list_by_automation_account(client):
    """Test case for variable_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/variables'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_variable_update(client):
    """Test case for variable_update

    
    """
    parameters = {"name":"name","properties":{"description":"description","value":"value"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/variables/{variable_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', variable_name='variable_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

