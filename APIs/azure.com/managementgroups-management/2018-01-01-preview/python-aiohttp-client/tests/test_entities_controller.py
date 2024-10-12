# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.entity_list_result import EntityListResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_entities_list(client):
    """Test case for entities_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skiptoken', 'skiptoken_example'),
                    ('groupName', 'group_name_example')]
    headers = { 
        'Accept': 'application/json',
        'cache_control': 'no-cache',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Management/getEntities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

