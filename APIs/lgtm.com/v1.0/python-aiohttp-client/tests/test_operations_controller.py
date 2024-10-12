# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation import Operation


pytestmark = pytest.mark.asyncio

async def test_get_operation(client):
    """Test case for get_operation

    Get operation status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1.0/operations/{operation_id}'.format(operation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

