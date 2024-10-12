# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.airport_response import AirportResponse


pytestmark = pytest.mark.asyncio

async def test_references_aircraft_by_aircraft_code_get(client):
    """Test case for references_aircraft_by_aircraft_code_get

    Aircraft
    """
    params = [('limit', '20'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/aircraft/{aircraft_code}'.format(aircraft_code='33P'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_airlines_by_airline_code_get(client):
    """Test case for references_airlines_by_airline_code_get

    Airlines
    """
    params = [('limit', '20'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/airlines/{airline_code}'.format(airline_code='LH'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_airports_by_airport_code_get(client):
    """Test case for references_airports_by_airport_code_get

    Airports
    """
    params = [('lang', 'lang_example'),
                    ('limit', '20'),
                    ('offset', '0'),
                    ('LHoperated', True)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/airports/{airport_code}'.format(airport_code='TXL'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_airports_nearest_by_latitude_and_longitude_get(client):
    """Test case for references_airports_nearest_by_latitude_and_longitude_get

    Nearest Airports
    """
    params = [('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/airports/nearest/{latitudelongitude}'.format(latitude=56, longitude=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_cities_by_city_code_get(client):
    """Test case for references_cities_by_city_code_get

    Cities
    """
    params = [('lang', 'lang_example'),
                    ('limit', '20'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/cities/{city_code}'.format(city_code='BER'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_references_countries_by_country_code_get(client):
    """Test case for references_countries_by_country_code_get

    Countries
    """
    params = [('lang', 'lang_example'),
                    ('limit', '20'),
                    ('offset', '0')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/references/countries/{country_code}'.format(country_code='DK'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

