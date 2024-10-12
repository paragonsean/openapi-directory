# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airports_search_response import AirportsSearchResponse
from openapi_server.models.cities_response import CitiesResponse
from openapi_server.models.continents_response import ContinentsResponse
from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_airport(client):
    """Test case for get_airport

    Search airports by country / Search nearby airports / Search an airport
    """
    params = [('language', 'language_example'),
                    ('location', 'location_example'),
                    ('radius', 100),
                    ('countrycode', 'countrycode_example'),
                    ('top_airports', True)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/airports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_autocomplete(client):
    """Test case for get_autocomplete

    Retrieve cities informations from a string / build an autocomplete
    """
    params = [('q', 'q_example'),
                    ('language', 'language_example'),
                    ('countrycode', 'countrycode_example'),
                    ('sort', population,desc)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cities/findcitiesfromtext',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cities(client):
    """Test case for get_cities

    Search all cities from lat/long or countrycode
    """
    params = [('language', 'language_example'),
                    ('countrycode', 'countrycode_example'),
                    ('location', 'location_example'),
                    ('radius', 20),
                    ('limit', 20),
                    ('offset', 0),
                    ('sort', distance,asc)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cities/findcitiesfromlatlong',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_continents(client):
    """Test case for get_continents

    Search all continents or one specific continent
    """
    params = [('language', 'language_example'),
                    ('continentcode', 'continentcode_example')]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/continents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_countries(client):
    """Test case for get_countries

    Search all countries or one specific country
    """
    params = [('language', 'language_example'),
                    ('countrycode', 'countrycode_example')]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_significant_cities(client):
    """Test case for get_significant_cities

    Search significant cities from lat/long or countrycode
    """
    params = [('language', 'language_example'),
                    ('pourcent', 0.5),
                    ('countrycode', 'countrycode_example'),
                    ('location', 'location_example'),
                    ('radius', 20),
                    ('limit', 20),
                    ('offset', 0),
                    ('sort', population,desc)]
    headers = { 
        'Accept': 'application/json',
        'x-api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/cities/significant',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

