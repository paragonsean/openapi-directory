# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_daemon_token200_response import GetDaemonToken200Response


pytestmark = pytest.mark.asyncio

async def test_get_daemon_token(client):
    """Test case for get_daemon_token

    Get a token for opening a daemon connection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/daemons/{daemon}/token'.format(daemon='daemon_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

