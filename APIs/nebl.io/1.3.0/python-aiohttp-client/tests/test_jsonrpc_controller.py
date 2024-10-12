# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rpc_request import RpcRequest
from openapi_server.models.rpc_response import RpcResponse


pytestmark = pytest.mark.asyncio

async def test_json_rpc(client):
    """Test case for json_rpc

    Send a JSON-RPC call to a localhost neblio-Qt or nebliod node
    """
    body = openapi_server.RpcRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

