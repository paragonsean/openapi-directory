# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_arrival_departure import TflApiPresentationEntitiesArrivalDeparture
from openapi_server.models.tfl_api_presentation_entities_disrupted_point import TflApiPresentationEntitiesDisruptedPoint
from openapi_server.models.tfl_api_presentation_entities_line_service_type import TflApiPresentationEntitiesLineServiceType
from openapi_server.models.tfl_api_presentation_entities_mode import TflApiPresentationEntitiesMode
from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server.models.tfl_api_presentation_entities_search_response import TflApiPresentationEntitiesSearchResponse
from openapi_server.models.tfl_api_presentation_entities_stop_point import TflApiPresentationEntitiesStopPoint
from openapi_server.models.tfl_api_presentation_entities_stop_point_category import TflApiPresentationEntitiesStopPointCategory
from openapi_server.models.tfl_api_presentation_entities_stop_point_route_section import TflApiPresentationEntitiesStopPointRouteSection
from openapi_server.models.tfl_api_presentation_entities_stop_points_response import TflApiPresentationEntitiesStopPointsResponse


pytestmark = pytest.mark.asyncio

async def test_stop_point_arrival_departures(client):
    """Test case for stop_point_arrival_departures

    Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only)
    """
    params = [('lineIds', ['line_ids_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/ArrivalDepartures'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_arrivals(client):
    """Test case for stop_point_arrivals

    Gets the list of arrival predictions for the given stop point id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/Arrivals'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_crowding(client):
    """Test case for stop_point_crowding

    Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.
    """
    params = [('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/Crowding/{line}'.format(id='id_example', line='line_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_direction(client):
    """Test case for stop_point_direction

    Returns the canonical direction, \"inbound\" or \"outbound\", for a given pair of stop point Ids in the direction from -&gt; to.
    """
    params = [('lineId', 'line_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/DirectionTo/{to_stop_point_id}'.format(id='id_example', to_stop_point_id='to_stop_point_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_disruption(client):
    """Test case for stop_point_disruption

    Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.
    """
    params = [('getFamily', True),
                    ('includeRouteBlockedStops', True),
                    ('flattenResponse', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{ids}/Disruption'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_disruption_by_mode(client):
    """Test case for stop_point_disruption_by_mode

    Gets a distinct list of disrupted stop points for the given modes
    """
    params = [('includeRouteBlockedStops', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Mode/{modes}/Disruption'.format(modes=['modes_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get(client):
    """Test case for stop_point_get

    Gets a list of StopPoints corresponding to the given list of stop ids.
    """
    params = [('includeCrowdingData', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{ids}'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_by_geo_point(client):
    """Test case for stop_point_get_by_geo_point

    Gets a list of StopPoints within {radius} by the specified criteria
    """
    params = [('stopTypes', ['stop_types_example']),
                    ('radius', 56),
                    ('useStopPointHierarchy', True),
                    ('modes', ['modes_example']),
                    ('categories', ['categories_example']),
                    ('returnLines', True),
                    ('location.lat', 3.4),
                    ('location.lon', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_by_mode(client):
    """Test case for stop_point_get_by_mode

    Gets a list of StopPoints filtered by the modes available at that StopPoint.
    """
    params = [('page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Mode/{modes}'.format(modes=['modes_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_by_sms(client):
    """Test case for stop_point_get_by_sms

    Gets a StopPoint for a given sms code.
    """
    params = [('output', 'output_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Sms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_by_type(client):
    """Test case for stop_point_get_by_type

    Gets all stop points of a given type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Type/{types}'.format(types=['types_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_by_type_with_pagination(client):
    """Test case for stop_point_get_by_type_with_pagination

    Gets all the stop points of given type(s) with a page number
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Type/{types}/page/{page}'.format(types=['types_example'], page=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_car_parks_by_id(client):
    """Test case for stop_point_get_car_parks_by_id

    Get car parks corresponding to the given stop point id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{stop_point_id}/CarParks'.format(stop_point_id='stop_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_service_types(client):
    """Test case for stop_point_get_service_types

    Gets the service types for a given stoppoint
    """
    params = [('id', 'id_example'),
                    ('lineIds', ['line_ids_example']),
                    ('modes', ['modes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/ServiceTypes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_get_taxi_ranks_by_ids(client):
    """Test case for stop_point_get_taxi_ranks_by_ids

    Gets a list of taxi ranks corresponding to the given stop point id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{stop_point_id}/TaxiRanks'.format(stop_point_id='stop_point_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_id_place_types_get(client):
    """Test case for stop_point_id_place_types_get

    Get a list of places corresponding to a given id and place types.
    """
    params = [('placeTypes', ['place_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/placeTypes'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_meta_categories(client):
    """Test case for stop_point_meta_categories

    Gets the list of available StopPoint additional information categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Meta/Categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_meta_modes(client):
    """Test case for stop_point_meta_modes

    Gets the list of available StopPoint modes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Meta/Modes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_meta_stop_types(client):
    """Test case for stop_point_meta_stop_types

    Gets the list of available StopPoint types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Meta/StopTypes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_reachable_from(client):
    """Test case for stop_point_reachable_from

    Gets Stopoints that are reachable from a station/line combination.
    """
    params = [('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/CanReachOnLine/{line_id}'.format(id='id_example', line_id='line_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_route(client):
    """Test case for stop_point_route

    Returns the route sections for all the lines that service the given stop point ids
    """
    params = [('serviceTypes', ['service_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/{id}/Route'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_search(client):
    """Test case for stop_point_search

    Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
    """
    params = [('modes', ['modes_example']),
                    ('faresOnly', True),
                    ('maxResults', 56),
                    ('lines', ['lines_example']),
                    ('includeHubs', True),
                    ('tflOperatedNationalRailStationsOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Search/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_point_search_get(client):
    """Test case for stop_point_search_get

    Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
    """
    params = [('query', 'query_example'),
                    ('modes', ['modes_example']),
                    ('faresOnly', True),
                    ('maxResults', 56),
                    ('lines', ['lines_example']),
                    ('includeHubs', True),
                    ('tflOperatedNationalRailStationsOnly', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/StopPoint/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

