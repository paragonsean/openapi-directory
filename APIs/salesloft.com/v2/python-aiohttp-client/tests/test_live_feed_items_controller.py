# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.live_feed_item import LiveFeedItem


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_third_party_live_feed_items_post(client):
    """Test case for v2_third_party_live_feed_items_post

    Create a live feed item
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'event_occurred_at': 'event_occurred_at_example',
        'idempotency_key': 'idempotency_key_example',
        'message': 'message_example',
        'subject_id': 56,
        'subject_type': 'subject_type_example',
        'user_guid': 'user_guid_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/third_party_live_feed_items',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

