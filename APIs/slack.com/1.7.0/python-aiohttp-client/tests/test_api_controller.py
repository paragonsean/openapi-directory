# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_test_error_schema import ApiTestErrorSchema
from openapi_server.models.api_test_success_schema import ApiTestSuccessSchema


pytestmark = pytest.mark.asyncio

async def test_api_test(client):
    """Test case for api_test

    
    """
    params = [('error', 'error_example'),
                    ('foo', 'foo_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api.test',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

