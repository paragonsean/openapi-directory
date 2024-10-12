# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aq_hourly import AQHourly
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_forecast_airqualitycity_idcity_id_get(client):
    """Test case for forecast_airqualitycity_idcity_id_get

    Returns 72 hour (hourly) Air Quality forecast - Given a City ID.
    """
    params = [('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/airquality?city_id={city_id}'.format(city_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_airqualitycitycitycountrycountry_get(client):
    """Test case for forecast_airqualitycitycitycountrycountry_get

    Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.
    """
    params = [('state', 'state_example'),
                    ('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/airquality?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_airqualitylatlatlonlon_get(client):
    """Test case for forecast_airqualitylatlatlonlon_get

    Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.
    """
    params = [('callback', 'param_callback_example'),
                    ('key', 'key_example'),
                    ('hours', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/airquality?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forecast_airqualitypostal_codepostal_code_get(client):
    """Test case for forecast_airqualitypostal_codepostal_code_get

    Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.
    """
    params = [('country', 'country_example'),
                    ('callback', 'param_callback_example'),
                    ('hours', 56),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/forecast/airquality?postal_code={postal_code}'.format(postal_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

