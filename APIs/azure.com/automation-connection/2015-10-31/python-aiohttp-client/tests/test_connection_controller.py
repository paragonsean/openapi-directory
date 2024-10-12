# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server.models.connection_create_or_update_parameters import ConnectionCreateOrUpdateParameters
from openapi_server.models.connection_list_by_automation_account_default_response import ConnectionListByAutomationAccountDefaultResponse
from openapi_server.models.connection_list_result import ConnectionListResult
from openapi_server.models.connection_update_parameters import ConnectionUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_connection_create_or_update(client):
    """Test case for connection_create_or_update

    
    """
    parameters = {"name":"name","properties":{"description":"description","connectionType":{"name":"name"},"fieldDefinitionValues":{"key":"fieldDefinitionValues"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_delete(client):
    """Test case for connection_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_get(client):
    """Test case for connection_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_list_by_automation_account(client):
    """Test case for connection_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connections'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_update(client):
    """Test case for connection_update

    
    """
    parameters = {"name":"name","properties":{"description":"description","fieldDefinitionValues":{"key":"fieldDefinitionValues"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connections/{connection_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_name='connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

