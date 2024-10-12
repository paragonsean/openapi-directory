# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.v3_departures_response import V3DeparturesResponse
from openapi_server.models.v3_error_response import V3ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_departures_get_for_stop(client):
    """Test case for departures_get_for_stop

    View departures for all routes from a stop
    """
    params = [('platform_numbers', [56]),
                    ('direction_id', 56),
                    ('gtfs', True),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('max_results', 56),
                    ('include_cancelled', True),
                    ('look_backwards', True),
                    ('expand', ['expand_example']),
                    ('include_geopath', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/departures/route_type/{route_type}/stop/{stop_id}'.format(route_type=56, stop_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_departures_get_for_stop_and_route(client):
    """Test case for departures_get_for_stop_and_route

    View departures for a specific route from a stop
    """
    params = [('direction_id', 56),
                    ('gtfs', True),
                    ('date_utc', '2013-10-20T19:20:30+01:00'),
                    ('max_results', 56),
                    ('include_cancelled', True),
                    ('look_backwards', True),
                    ('expand', ['expand_example']),
                    ('include_geopath', True),
                    ('token', 'token_example'),
                    ('devid', 'devid_example'),
                    ('signature', 'signature_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v3/departures/route_type/{route_type}/stop/{stop_id}/route/{route_id}'.format(route_type=56, stop_id=56, route_id='route_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

