# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.node_peer import NodePeer


pytestmark = pytest.mark.asyncio

async def test_get_peers_list(client):
    """Test case for get_peers_list

    Lists known peers sorted by block height
    """
    params = [('unreachable', False),
                    ('closedApi', False),
                    ('limit', 50)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/peers/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

