# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_query_keys_result import ListQueryKeysResult


pytestmark = pytest.mark.asyncio

async def test_query_keys_list(client):
    """Test case for query_keys_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Search/searchServices/{service_name}/listQueryKeys'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

