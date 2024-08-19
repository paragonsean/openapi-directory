# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_errors_response import ListErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_list_errors(client):
    """Test case for list_errors

    List Errors
    """
    params = [('filters[]', ['filters_example']),
                    ('timeframe[]', ['timeframe_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/data/v1/errors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

