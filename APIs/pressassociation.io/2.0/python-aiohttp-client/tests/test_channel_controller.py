# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_channel(client):
    """Test case for get_channel

    Channel Detail
    """
    params = [('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/channel/{channel_id}'.format(channel_id='channel_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_channels(client):
    """Test case for list_channels

    Channel Collection
    """
    params = [('platformId', 'd3b26caa-8c7d-5f97-9eff-40fcf1a6f8d3'),
                    ('regionId', 'afa4f624-da9b-54ce-b514-570345dbbdce'),
                    ('aliases', True),
                    ('date', '2018-09-15'),
                    ('scheduleStart', '2015-05-05T00:00:00'),
                    ('scheduleEnd', '2015-05-06T00:00:00'),
                    ('scheduleUpdatedSince', '2015-05-05T00:00:00')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/channel',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

