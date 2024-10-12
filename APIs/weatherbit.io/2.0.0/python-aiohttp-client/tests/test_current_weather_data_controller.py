# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.current_obs_group import CurrentObsGroup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_currentcitiescities_get(client):
    """Test case for currentcitiescities_get

    Returns a group of observations given a list of cities
    """
    params = [('units', 'units_example'),
                    ('marine', 'marine_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?cities={cities}'.format(cities='cities_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentcity_idcity_id_get(client):
    """Test case for currentcity_idcity_id_get

    Returns a current observation by city id.
    """
    params = [('units', 'units_example'),
                    ('include', 'include_example'),
                    ('marine', 'marine_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?city_id={city_id}'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentcitycitycountrycountry_get(client):
    """Test case for currentcitycitycountrycountry_get

    Returns a Current Observation - Given City and/or State, Country.
    """
    params = [('include', 'include_example'),
                    ('state', 'state_example'),
                    ('marine', 'marine_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentlatlatlonlon_get(client):
    """Test case for currentlatlatlonlon_get

    Returns a Current Observation - Given a lat/lon.
    """
    params = [('include', 'include_example'),
                    ('marine', 'marine_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentpointspoints_get(client):
    """Test case for currentpointspoints_get

    Returns a group of observations given a list of points in the format (lat1, lon1), (lat2, lon2), (latN, lonN), ...
    """
    params = [('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?points={points}'.format(points='points_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentpostal_codepostal_code_get(client):
    """Test case for currentpostal_codepostal_code_get

    Returns a current observation by postal code.
    """
    params = [('country', 'country_example'),
                    ('include', 'include_example'),
                    ('marine', 'marine_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?postal_code={postal_code}'.format(postal_code='postal_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentstationsstations_get(client):
    """Test case for currentstationsstations_get

    Returns a group of observations given a list of stations
    """
    params = [('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?stations={stations}'.format(stations='stations_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_currentstationstation_get(client):
    """Test case for currentstationstation_get

    Returns a Current Observation. - Given a station ID.
    """
    params = [('include', 'include_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/current?station={station}'.format(station='station_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

