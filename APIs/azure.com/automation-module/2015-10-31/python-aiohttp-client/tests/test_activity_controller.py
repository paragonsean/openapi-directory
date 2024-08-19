# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_list_result import ActivityListResult
from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_activity_get(client):
    """Test case for activity_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}/activities/{activity_name}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', activity_name='activity_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_by_module(client):
    """Test case for activity_list_by_module

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/modules/{module_name}/activities'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', module_name='module_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

