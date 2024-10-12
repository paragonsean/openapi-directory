# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus


pytestmark = pytest.mark.asyncio

async def test_delete_cache(client):
    """Test case for delete_cache

    Clear cache by key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/cache/{key}'.format(key='any key'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

