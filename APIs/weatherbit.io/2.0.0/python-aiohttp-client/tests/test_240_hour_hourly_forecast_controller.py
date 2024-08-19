# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.forecast_hourly import ForecastHourly


pytestmark = pytest.mark.asyncio

async def test_forecast_hourlycity_idcity_id_get(client):
    """Test case for forecast_hourlycity_idcity_id_get

    Returns an hourly forecast - Given a City ID.
    """
    params = [('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/hourly?city_id={city_id}'.format(city_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_hourlycitycitycountrycountry_get(client):
    """Test case for forecast_hourlycitycitycountrycountry_get

    Returns an hourly forecast - Given City and/or State, Country.
    """
    params = [('state', 'state_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/hourly?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_hourlylatlatlonlon_get(client):
    """Test case for forecast_hourlylatlatlonlon_get

    Returns an hourly forecast - Given a lat/lon.
    """
    params = [('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example'),
                    ('hours', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/hourly?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_hourlypostal_codepostal_code_get(client):
    """Test case for forecast_hourlypostal_codepostal_code_get

    Returns an hourly forecast - Given a Postal Code.
    """
    params = [('country', 'country_example'),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/hourly?postal_code={postal_code}'.format(postal_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

