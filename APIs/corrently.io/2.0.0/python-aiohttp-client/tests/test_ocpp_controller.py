# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.easee_charger import EaseeCharger


pytestmark = pytest.mark.asyncio

async def test_ocpp_sessions(client):
    """Test case for ocpp_sessions

    Last Session Info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/alternative/ocpp/lastSessions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

