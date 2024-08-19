# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.forecast_day import ForecastDay


pytestmark = pytest.mark.asyncio

async def test_forecast_dailycity_idcity_id_get(client):
    """Test case for forecast_dailycity_idcity_id_get

    Returns a daily forecast - Given a City ID.
    """
    params = [('days', 3.4),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/daily?city_id={city_id}'.format(city_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_dailycitycitycountrycountry_get(client):
    """Test case for forecast_dailycitycitycountrycountry_get

    Returns a daily forecast - Given City and/or State, Country.
    """
    params = [('state', 'state_example'),
                    ('days', 3.4),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/daily?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_dailylatlatlonlon_get(client):
    """Test case for forecast_dailylatlatlonlon_get

    Returns a daily forecast - Given Lat/Lon.
    """
    params = [('days', 3.4),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/daily?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_dailypostal_codepostal_code_get(client):
    """Test case for forecast_dailypostal_codepostal_code_get

    Returns a daily forecast - Given a Postal Code.
    """
    params = [('country', 'country_example'),
                    ('days', 3.4),
                    ('units', 'units_example'),
                    ('lang', 'lang_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/daily?postal_code={postal_code}'.format(postal_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

