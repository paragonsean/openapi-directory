# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_channels(client):
    """Test case for get_channels

    List all the channels.
    """
    params = [('region', 'region_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/channels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_highlights_by_channel(client):
    """Test case for get_highlights_by_channel

    List the highlights for a channel.
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('live', True),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/channels/{channel}/highlights'.format(channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_schedule_by_channel(client):
    """Test case for get_schedule_by_channel

    Get schedule by channel
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/channels/{channel}/schedule/{_date}'.format(channel='channel_example', _date='_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

