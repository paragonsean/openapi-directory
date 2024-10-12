# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_custom_events_analytics_0(client):
    """Test case for custom_events_analytics_0

    Custom Events Analytics
    """
    params = [('event', 'event_name'),
                    ('length', '24'),
                    ('unit', 'hour'),
                    ('ending_at', '2014-12-10T23:59:59-05:00'),
                    ('app_id', '{{app_identifier}}'),
                    ('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/events/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_events_list_0(client):
    """Test case for custom_events_list_0

    Custom Events List
    """
    params = [('page', '3')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/events/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

