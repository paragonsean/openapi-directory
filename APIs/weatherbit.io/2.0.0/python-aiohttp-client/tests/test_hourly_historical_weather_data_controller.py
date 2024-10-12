# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.history import History


pytestmark = pytest.mark.asyncio

async def test_history_hourlycity_idcity_id_get(client):
    """Test case for history_hourlycity_idcity_id_get

    Returns Historical Observations - Given a City ID
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('tz', 'tz_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/hourly?city_id={city_id}'.format(city_id='city_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_hourlycitycitycountrycountry_get(client):
    """Test case for history_hourlycitycitycountrycountry_get

    Returns Historical Observations - Given City and/or State, Country.
    """
    params = [('state', 'state_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('tz', 'tz_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/hourly?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_hourlylatlatlonlon_get(client):
    """Test case for history_hourlylatlatlonlon_get

    Returns Historical Observations - Given a lat/lon.
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('tz', 'tz_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/hourly?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_hourlypostal_codepostal_code_get(client):
    """Test case for history_hourlypostal_codepostal_code_get

    Returns Historical Observations - Given a Postal Code
    """
    params = [('country', 'country_example'),
                    ('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('tz', 'tz_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/hourly?postal_code={postal_code}'.format(postal_code='postal_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_hourlystationstation_get(client):
    """Test case for history_hourlystationstation_get

    Returns Historical Observations - Given a station ID.
    """
    params = [('start_date', 'start_date_example'),
                    ('end_date', 'end_date_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('tz', 'tz_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/hourly?station={station}'.format(station='station_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

