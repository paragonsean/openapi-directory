# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_disruption import TflApiPresentationEntitiesDisruption
from openapi_server.models.tfl_api_presentation_entities_line import TflApiPresentationEntitiesLine
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server.models.tfl_api_presentation_entities_route_search_response import TflApiPresentationEntitiesRouteSearchResponse
from openapi_server.models.tfl_api_presentation_entities_route_sequence import TflApiPresentationEntitiesRouteSequence
from openapi_server.models.tfl_api_presentation_entities_status_severity import TflApiPresentationEntitiesStatusSeverity
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint
from openapi_server.models.tfl_api_presentation_entities_timetable_response import TflApiPresentationEntitiesTimetableResponse


pytestmark = pytest.mark.asyncio

async def test_line_arrivals(client):
    """Test case for line_arrivals

    Get the list of arrival predictions for given line ids based at the given stop
    """
    params = [('direction', 'direction_example'),
                    ('destinationStationId', 'destination_station_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}/Arrivals/{stop_point_id}'.format(ids=['ids_example'], stop_point_id='stop_point_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_disruption(client):
    """Test case for line_disruption

    Get disruptions for the given line ids
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}/Disruption'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_disruption_by_mode(client):
    """Test case for line_disruption_by_mode

    Get disruptions for all lines of the given modes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Mode/{modes}/Disruption'.format(modes=['modes_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_get(client):
    """Test case for line_get

    Gets lines that match the specified line ids.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_get_by_mode(client):
    """Test case for line_get_by_mode

    Gets lines that serve the given modes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Mode/{modes}'.format(modes=['modes_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_line_routes_by_ids(client):
    """Test case for line_line_routes_by_ids

    Get all valid routes for given line ids, including the name and id of the originating and terminating stops for each route.
    """
    params = [('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}/Route'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_meta_disruption_categories(client):
    """Test case for line_meta_disruption_categories

    Gets a list of valid disruption categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Meta/DisruptionCategories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_meta_modes(client):
    """Test case for line_meta_modes

    Gets a list of valid modes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Meta/Modes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_meta_service_types(client):
    """Test case for line_meta_service_types

    Gets a list of valid ServiceTypes to filter on
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Meta/ServiceTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_meta_severity(client):
    """Test case for line_meta_severity

    Gets a list of valid severity codes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Meta/Severity',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_route(client):
    """Test case for line_route

    Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.
    """
    params = [('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Route',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_route_by_mode(client):
    """Test case for line_route_by_mode

    Gets all lines and their valid routes for given modes, including the name and id of the originating and terminating stops for each route
    """
    params = [('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Mode/{modes}/Route'.format(modes=['modes_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_route_sequence(client):
    """Test case for line_route_sequence

    Gets all valid routes for given line id, including the sequence of stops on each route.
    """
    params = [('serviceTypes', ['service_types_example']),
                    ('excludeCrowding', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{id}/Route/Sequence/{direction}'.format(id='id_example', direction='direction_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_search(client):
    """Test case for line_search

    Search for lines or routes matching the query string
    """
    params = [('modes', ['modes_example']),
                    ('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_status(client):
    """Test case for line_status

    Gets the line status for given line ids during the provided dates e.g Minor Delays
    """
    params = [('detail', True),
                    ('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('dateRange.startDate', '2013-10-20T19:20:30+01:00'),
                    ('dateRange.endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}/Status/{start_date}/to/{end_date}'.format(ids=['ids_example'], start_date2='start_date_example', end_date2='end_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_status_by_ids(client):
    """Test case for line_status_by_ids

    Gets the line status of for given line ids e.g Minor Delays
    """
    params = [('detail', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{ids}/Status'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_status_by_mode(client):
    """Test case for line_status_by_mode

    Gets the line status of for all lines for the given modes
    """
    params = [('detail', True),
                    ('severityLevel', 'severity_level_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Mode/{modes}/Status'.format(modes=['modes_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_status_by_severity(client):
    """Test case for line_status_by_severity

    Gets the line status for all lines with a given severity              A list of valid severity codes can be obtained from a call to Line/Meta/Severity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/Status/{severity}'.format(severity=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_stop_points(client):
    """Test case for line_stop_points

    Gets a list of the stations that serve the given line id
    """
    params = [('tflOperatedNationalRailStationsOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{id}/StopPoints'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_timetable(client):
    """Test case for line_timetable

    Gets the timetable for a specified station on the give line
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{id}/Timetable/{from_stop_point_id}'.format(from_stop_point_id='from_stop_point_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_line_timetable_to(client):
    """Test case for line_timetable_to

    Gets the timetable for a specified station on the give line with specified destination
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Line/{id}/Timetable/{from_stop_point_id}/to/{to_stop_point_id}'.format(from_stop_point_id='from_stop_point_id_example', id='id_example', to_stop_point_id='to_stop_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

