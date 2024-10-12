# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_into_an_item_request import CheckIntoAnItemRequest


pytestmark = pytest.mark.asyncio

async def test_check_into_an_item(client):
    """Test case for check_into_an_item

    Check into an item
    """
    body = openapi_server.CheckIntoAnItemRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/checkin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_any_active_checkins(client):
    """Test case for delete_any_active_checkins

    Delete any active checkins
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/checkin',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

