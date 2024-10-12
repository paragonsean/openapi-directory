# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.resource_owner import ResourceOwner


pytestmark = pytest.mark.asyncio

async def test_get_resource_owner(client):
    """Test case for get_resource_owner

    Retrieve a resource owner by ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/resourceOwners/{resource_owner_id}'.format(resource_owner_id='resource_owner_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

