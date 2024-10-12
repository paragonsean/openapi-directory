# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_update200_response import AttributeUpdate200Response
from openapi_server.models.bridge_delete200_response import BridgeDelete200Response


pytestmark = pytest.mark.asyncio

async def test_bridge_delete(client):
    """Test case for bridge_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/bridge.delete.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bridge_update(client):
    """Test case for bridge_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'store_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.1/bridge.update.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

