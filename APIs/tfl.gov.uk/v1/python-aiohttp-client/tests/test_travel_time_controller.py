# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_travel_time_get_compare_overlay(client):
    """Test case for travel_time_get_compare_overlay

    Gets the TravelTime overlay.
    """
    params = [('scenarioTitle', 'scenario_title_example'),
                    ('timeOfDayId', 'time_of_day_id_example'),
                    ('modeId', 'mode_id_example'),
                    ('direction', 'direction_example'),
                    ('travelTimeInterval', 56),
                    ('compareType', 'compare_type_example'),
                    ('compareValue', 'compare_value_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/TravelTimes/compareOverlay/{z}/mapcenter/{map_center_lat}/{map_center_lon}/pinlocation/{pin_lat}/{pin_lon}/dimensions/{width}/{height}'.format(z=56, pin_lat=3.4, pin_lon=3.4, map_center_lat=3.4, map_center_lon=3.4, width=56, height=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_time_get_overlay(client):
    """Test case for travel_time_get_overlay

    Gets the TravelTime overlay.
    """
    params = [('scenarioTitle', 'scenario_title_example'),
                    ('timeOfDayId', 'time_of_day_id_example'),
                    ('modeId', 'mode_id_example'),
                    ('direction', 'direction_example'),
                    ('travelTimeInterval', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/TravelTimes/overlay/{z}/mapcenter/{map_center_lat}/{map_center_lon}/pinlocation/{pin_lat}/{pin_lon}/dimensions/{width}/{height}'.format(z=56, pin_lat=3.4, pin_lon=3.4, map_center_lat=3.4, map_center_lon=3.4, width=56, height=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

