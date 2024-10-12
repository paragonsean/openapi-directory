# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_schedule(client):
    """Test case for list_schedule

    Schedule Collection
    """
    params = [('channelId', 'channel_id_example'),
                    ('start', '2015-05-05T00:00:00'),
                    ('end', '2015-05-06T00:00:00'),
                    ('aliases', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/schedule',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

