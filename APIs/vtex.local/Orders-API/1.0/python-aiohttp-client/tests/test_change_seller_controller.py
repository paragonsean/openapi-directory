# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_window_to_change_seller_request import UpdateWindowToChangeSellerRequest


pytestmark = pytest.mark.asyncio

async def test_get_window_to_change_seller(client):
    """Test case for get_window_to_change_seller

    Get window to change seller
    """
    headers = { 
        'Accept': 'text/plain',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/checkout/pvt/configuration/window-to-change-seller',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_window_to_change_seller(client):
    """Test case for update_window_to_change_seller

    Update window to change seller
    """
    body = {"waitingTime":4}
    headers = { 
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/checkout/pvt/configuration/window-to-change-seller',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

