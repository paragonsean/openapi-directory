# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_usage_get_usage(client):
    """Test case for usage_get_usage

    Returns usage records for specified subscription and resource groups
    """
    params = [('lastId', 'last_id_example'),
                    ('batchSize', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web.Admin/environments/{environment_name}/usage'.format(resource_group_name='resource_group_name_example', environment_name='environment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

