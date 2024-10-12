# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_send_events_response import GetSendEventsResponse


pytestmark = pytest.mark.asyncio

async def test_v3_asset_management_assets_send_events_get(client):
    """Test case for v3_asset_management_assets_send_events_get

    
    """
    params = [('last_offset', '2013-10-20T19:20:30+01:00'),
                    ('event_count', 56)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/asset-management/assets/send-events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

