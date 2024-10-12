# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.global_blackout_window_status import GlobalBlackoutWindowStatus


pytestmark = pytest.mark.asyncio

async def test_get_blackout_window_status(client):
    """Test case for get_blackout_window_status

    Get current status of global blackout window
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/blackout_window',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_toggle_blackout_window(client):
    """Test case for toggle_blackout_window

    Starts or stops the global blackout window in local Rubrik cluster
    """
    body = {"isGlobalBlackoutActive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/blackout_window',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

