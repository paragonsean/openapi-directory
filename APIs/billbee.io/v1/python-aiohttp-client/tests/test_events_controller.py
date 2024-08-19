# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_event_api_get_list(client):
    """Test case for event_api_get_list

    Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.
    """
    params = [('minDate', '2013-10-20T19:20:30+01:00'),
                    ('maxDate', '2013-10-20T19:20:30+01:00'),
                    ('page', 56),
                    ('pageSize', 56),
                    ('typeId', [56]),
                    ('orderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

