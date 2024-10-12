# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.keys_metadata_representation import KeysMetadataRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_keys_get(client):
    """Test case for realm_keys_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/keys'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

