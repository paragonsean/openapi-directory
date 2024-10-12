# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.presence_message import PresenceMessage


pytestmark = pytest.mark.asyncio

async def test_get_messages_by_channel(client):
    """Test case for get_messages_by_channel

    Get message history for a channel
    """
    params = [('format', 'format_example'),
                    ('start', 'start_example'),
                    ('limit', 56),
                    ('end', 'now'),
                    ('direction', backwards)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/messages'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_presence_history_of_channel(client):
    """Test case for get_presence_history_of_channel

    Get presence history of a channel
    """
    params = [('format', 'format_example'),
                    ('start', 'start_example'),
                    ('limit', 56),
                    ('end', 'now'),
                    ('direction', backwards)]
    headers = { 
        'Accept': 'application/json',
        'x_ably_version': 'x_ably_version_example',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/presence/history'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

