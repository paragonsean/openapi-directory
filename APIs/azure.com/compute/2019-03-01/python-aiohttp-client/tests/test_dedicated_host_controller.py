# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dedicated_host_list_result import DedicatedHostListResult


pytestmark = pytest.mark.asyncio

async def test_dedicated_hosts_list_by_host_group(client):
    """Test case for dedicated_hosts_list_by_host_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/hostGroups/{host_group_name}/hosts'.format(resource_group_name='resource_group_name_example', host_group_name='host_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

