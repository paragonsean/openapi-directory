# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.linked_workspace import LinkedWorkspace
from openapi_server.models.linked_workspace_get_default_response import LinkedWorkspaceGetDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_linked_workspace_get(client):
    """Test case for linked_workspace_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/linkedWorkspace'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

