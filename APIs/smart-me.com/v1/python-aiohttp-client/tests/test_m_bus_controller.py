# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.m_bus_data import MBusData


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_m_bus_post(client):
    """Test case for m_bus_post

    M-BUS API: Adds data of a M-BUS Meter to the smart-me Cloud.              Just send us the M-BUS Telegram (RSP_UD) and we will do the Rest.
    """
    body = {"Telegram":"Telegram","Date":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/MBus',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

