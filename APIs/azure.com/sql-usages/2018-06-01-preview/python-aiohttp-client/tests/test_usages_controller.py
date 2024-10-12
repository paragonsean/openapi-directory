# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.usage_list_result import UsageListResult


pytestmark = pytest.mark.asyncio

async def test_usages_list_by_instance_pool(client):
    """Test case for usages_list_by_instance_pool

    
    """
    params = [('expandChildren', True),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/instancePools/{instance_pool_name}/usages'.format(resource_group_name='resource_group_name_example', instance_pool_name='instance_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

