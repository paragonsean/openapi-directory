# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channels_entity import ChannelsEntity
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_channels_entity import EventsChannelsEntity


pytestmark = pytest.mark.asyncio

async def test_fetch_all_channels(client):
    """Test case for fetch_all_channels

    Find all channels
    """
    params = [('label', 'label_example'),
                    ('show_ignored', False),
                    ('sort', label),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_all_events_channels(client):
    """Test case for fetch_all_events_channels

    Find all channels for one event
    """
    params = [('show_ignored', False),
                    ('page_size', 25)]
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/channels'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_channel(client):
    """Test case for fetch_one_channel

    Get one channel by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'accept_language': en,
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/channels/{channel_id}'.format(channel_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_one_event_channel(client):
    """Test case for fetch_one_event_channel

    Get one event channel by ID
    """
    headers = { 
        'Accept': 'application/hal+json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events/{event_id}/channels/{channel_id}'.format(event_id=56, channel_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

