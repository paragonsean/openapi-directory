# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.near_earth_object_list import NearEarthObjectList


pytestmark = pytest.mark.asyncio

async def test_retrieve_near_earth_object_feed(client):
    """Test case for retrieve_near_earth_object_feed

    Find Near Earth Objects by date
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('detailed', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/feed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_neo_feed_today(client):
    """Test case for retrieve_neo_feed_today

    Find Near Earth Objects for today
    """
    params = [('detailed', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1/feed/today',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

