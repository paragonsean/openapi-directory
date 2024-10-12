# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operations import Operations


pytestmark = pytest.mark.asyncio

async def test_fetch_operations(client):
    """Test case for fetch_operations

    Retrieve the operations accessible to a a given user.
    """
    params = [('resourceOwnerId', 'resource_owner_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/operations/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

