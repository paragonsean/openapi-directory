# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_type import ConnectionType
from openapi_server.models.connection_type_create_or_update_parameters import ConnectionTypeCreateOrUpdateParameters
from openapi_server.models.connection_type_list_by_automation_account_default_response import ConnectionTypeListByAutomationAccountDefaultResponse
from openapi_server.models.connection_type_list_result import ConnectionTypeListResult


pytestmark = pytest.mark.asyncio

async def test_connection_type_create_or_update(client):
    """Test case for connection_type_create_or_update

    
    """
    parameters = {"name":"name","properties":{"isGlobal":True,"fieldDefinitions":{"key":{"isEncrypted":True,"isOptional":True,"type":"type"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connectionTypes/{connection_type_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_type_name='connection_type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_type_delete(client):
    """Test case for connection_type_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connectionTypes/{connection_type_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_type_name='connection_type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_type_get(client):
    """Test case for connection_type_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connectionTypes/{connection_type_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', connection_type_name='connection_type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_type_list_by_automation_account(client):
    """Test case for connection_type_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/connectionTypes'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

