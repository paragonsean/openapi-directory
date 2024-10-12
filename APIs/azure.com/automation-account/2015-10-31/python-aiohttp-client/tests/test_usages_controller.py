# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.usage_list_result import UsageListResult


pytestmark = pytest.mark.asyncio

async def test_usages_list_by_automation_account(client):
    """Test case for usages_list_by_automation_account

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/usages'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

