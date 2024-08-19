# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse
from openapi_server.models.type_field_list_result import TypeFieldListResult


pytestmark = pytest.mark.asyncio

async def test_object_data_types_list_fields_by_module_and_type(client):
    """Test case for object_data_types_list_fields_by_module_and_type

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}/objectDataTypes/{type_name}/fields'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', type_name='type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_object_data_types_list_fields_by_type(client):
    """Test case for object_data_types_list_fields_by_type

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/objectDataTypes/{type_name}/fields'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', type_name='type_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

