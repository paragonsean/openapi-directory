# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_segment_analytics_0(client):
    """Test case for segment_analytics_0

    Segment Analytics
    """
    params = [('segment_id', '{{segment_identifier}}'),
                    ('length', '14'),
                    ('ending_at', '2018-06-27T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_segment_details_0(client):
    """Test case for segment_details_0

    Segment Details
    """
    params = [('segment_id', '{{segment_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_segment_list_0(client):
    """Test case for segment_list_0

    Segment List
    """
    params = [('page', '1'),
                    ('sort_direction', 'desc')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/segments/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

