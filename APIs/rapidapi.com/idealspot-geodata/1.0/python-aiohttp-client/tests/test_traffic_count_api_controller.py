# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_road_segments import SearchRoadSegments
from openapi_server.models.vehicle_traffic_countsfor_road_segment import VehicleTrafficCountsforRoadSegment


pytestmark = pytest.mark.asyncio

async def test_fetch_nearest_road_segments(client):
    """Test case for fetch_nearest_road_segments

    Fetch Nearest Road Segments
    """
    params = [('n', 56)]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/traffic/roads/nearest/{latitude}/{longitude}'.format(latitude=3.4, longitude=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vehicle_traffic_countsfor_road_segment(client):
    """Test case for vehicle_traffic_countsfor_road_segment

    Vehicle Traffic Counts for Road Segment
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/traffic/counts/{segment_id}'.format(segment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

