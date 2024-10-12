# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_throttled import ErrorThrottled
from openapi_server.models.network_unblock import NetworkUnblock
from openapi_server.models.network_unblock422_response import NetworkUnblock422Response
from openapi_server.models.network_unblock_response_forbidden import NetworkUnblockResponseForbidden
from openapi_server.models.network_unblock_response_not_found import NetworkUnblockResponseNotFound
from openapi_server.models.network_unblock_response_ok import NetworkUnblockResponseOk


pytestmark = pytest.mark.asyncio

async def test_network_unblock(client):
    """Test case for network_unblock

    Request a network unblock
    """
    body = openapi_server.NetworkUnblock()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/verify/network-unblock',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

