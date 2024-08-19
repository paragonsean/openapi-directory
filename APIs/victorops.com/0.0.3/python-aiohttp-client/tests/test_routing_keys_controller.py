# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_routing_keys_response import ListRoutingKeysResponse


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_org_routing_keys_get(client):
    """Test case for api_public_v1_org_routing_keys_get

    List routing keys with associated teams
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/org/routing-keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

