# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_events200_response import GetEvents200Response


pytestmark = pytest.mark.asyncio

async def test_get_events(client):
    """Test case for get_events

    Get events on a resource
    """
    params = [('resource', '12345'),
                    ('sync', 'de4774f6915eae04714ca93bb2f5ee81'),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

