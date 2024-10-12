# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.label import Label


pytestmark = pytest.mark.asyncio

async def test_get_active_sessions(client):
    """Test case for get_active_sessions

    Gets a list of active sessions
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/rtc/sessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

