# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.process import Process


pytestmark = pytest.mark.asyncio

async def test_processes_list(client):
    """Test case for processes_list

    Get process list.
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/processes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

