# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_stop_response import V3StopResponse
from openapi_server.models.v3_stops_by_distance_response import V3StopsByDistanceResponse
from openapi_server.models.v3_stops_on_route_response import V3StopsOnRouteResponse


pytestmark = pytest.mark.asyncio

async def test_stops_stop_details(client):
    """Test case for stops_stop_details

    View facilities at a specific stop (Metro and V/Line stations only)
    """
    params = [('stop_location', True),
                    ('stop_amenities', True),
                    ('stop_accessibility', True),
                    ('stop_contact', True),
                    ('stop_ticket', True),
                    ('gtfs', True),
                    ('stop_staffing', True),
                    ('stop_disruptions', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/stops/{stop_id}/route_type/{route_type}'.format(stop_id=56, route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stops_stops_by_geolocation(client):
    """Test case for stops_stops_by_geolocation

    View all stops near a specific location
    """
    params = [('route_types', [56]),
                    ('max_results', 56),
                    ('max_distance', 3.4),
                    ('stop_disruptions', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/stops/location/{latitudelongitude}'.format(latitude=3.4, longitude=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stops_stops_for_route(client):
    """Test case for stops_stops_for_route

    View all stops on a specific route
    """
    params = [('direction_id', 56),
                    ('stop_disruptions', True),
                    ('include_geopath', True),
                    ('geopath_utc', '2013-10-20T19:20:30+01:00'),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/stops/route/{route_id}/route_type/{route_type}'.format(route_id=56, route_type=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

