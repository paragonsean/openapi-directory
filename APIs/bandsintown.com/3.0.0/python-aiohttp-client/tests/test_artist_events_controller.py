# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.event_data import EventData


pytestmark = pytest.mark.asyncio

async def test_artist_events(client):
    """Test case for artist_events

    Get upcoming, past, or all artist events, or events within a date range
    """
    params = [('app_id', 'app_id_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/artists/{artistname}/events'.format(artistname='artistname_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

