# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_eula_accept(client):
    """Test case for eula_accept

    Accepts the EULA
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/plan/api/Eula/Accept',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

