# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_road_corridor import TflApiPresentationEntitiesRoadCorridor
from openapi_server.models.tfl_api_presentation_entities_road_disruption import TflApiPresentationEntitiesRoadDisruption
from openapi_server.models.tfl_api_presentation_entities_status_severity import TflApiPresentationEntitiesStatusSeverity


pytestmark = pytest.mark.asyncio

async def test_road_disrupted_streets(client):
    """Test case for road_disrupted_streets

    Gets a list of disrupted streets. If no date filters are provided, current disruptions are returned.
    """
    params = [('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/all/Street/Disruption',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_disruption(client):
    """Test case for road_disruption

    Get active disruptions, filtered by road ids
    """
    params = [('stripContent', True),
                    ('severities', ['severities_example']),
                    ('categories', ['categories_example']),
                    ('closures', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/{ids}/Disruption'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_disruption_by_id(client):
    """Test case for road_disruption_by_id

    Gets a list of active disruptions filtered by disruption Ids.
    """
    params = [('stripContent', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/all/Disruption/{disruption_ids}'.format(disruption_ids=['disruption_ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_get(client):
    """Test case for road_get

    Gets all roads managed by TfL
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_ids_get(client):
    """Test case for road_ids_get

    Gets the road with the specified id (e.g. A1)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/{ids}'.format(ids=['ids_example']),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_meta_categories(client):
    """Test case for road_meta_categories

    Gets a list of valid RoadDisruption categories
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/Meta/Categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_meta_severities(client):
    """Test case for road_meta_severities

    Gets a list of valid RoadDisruption severity codes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/Meta/Severities',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_road_status(client):
    """Test case for road_status

    Gets the specified roads with the status aggregated over the date range specified, or now until the end of today if no dates are passed.
    """
    params = [('dateRangeNullable.startDate', '2013-10-20T19:20:30+01:00'),
                    ('dateRangeNullable.endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Road/{ids}/Status'.format(ids=['ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

