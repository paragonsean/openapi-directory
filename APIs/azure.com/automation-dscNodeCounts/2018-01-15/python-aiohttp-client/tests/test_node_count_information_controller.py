# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.node_count_information_get_default_response import NodeCountInformationGetDefaultResponse
from openapi_server.models.node_counts import NodeCounts


pytestmark = pytest.mark.asyncio

async def test_node_count_information_get(client):
    """Test case for node_count_information_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Automation/automationAccounts/{automation_account_name}/nodecounts/{count_type}'.format(resource_group_name='resource_group_name_example', automation_account_name='automation_account_name_example', count_type='count_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

