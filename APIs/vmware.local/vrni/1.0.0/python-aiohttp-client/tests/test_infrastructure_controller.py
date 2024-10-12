# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.node import Node
from openapi_server.models.node_list_result import NodeListResult


pytestmark = pytest.mark.asyncio

async def test_get_node(client):
    """Test case for get_node

    Show node details
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/infra/nodes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_nodes(client):
    """Test case for list_nodes

    List nodes
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/infra/nodes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

