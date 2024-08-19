# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace


pytestmark = pytest.mark.asyncio

async def test_bike_point_get(client):
    """Test case for bike_point_get

    Gets the bike point with the given id.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BikePoint/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bike_point_get_all(client):
    """Test case for bike_point_get_all

    Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0 indicates broken docks.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BikePoint',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bike_point_search(client):
    """Test case for bike_point_search

    Search for bike stations by their name, a bike point's name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id.
    """
    params = [('query', 'query_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/BikePoint/Search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

