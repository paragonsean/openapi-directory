# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aq_current_group import AQCurrentGroup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_history_airqualitycity_idcity_id_get(client):
    """Test case for history_airqualitycity_idcity_id_get

    Returns 72 hours of historical air quality conditions - Given a City ID.
    """
    params = [('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/airquality?city_id={city_id}'.format(city_id=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_airqualitycitycitycountrycountry_get(client):
    """Test case for history_airqualitycitycitycountrycountry_get

    Returns 72 hours of historical quality conditions - Given City and/or State, Country.
    """
    params = [('state', 'state_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/airquality?city={city}&country={country}'.format(city='city_example', country='country_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_airqualitylatlatlonlon_get(client):
    """Test case for history_airqualitylatlatlonlon_get

    Returns 72 hours of historical air quality conditions - Given a lat/lon.
    """
    params = [('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/airquality?lat={lat}&lon={lon}'.format(lat=3.4, lon=3.4),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_history_airqualitypostal_codepostal_code_get(client):
    """Test case for history_airqualitypostal_codepostal_code_get

    Returns 72 hours of historical air quality conditions - Given a Postal Code.
    """
    params = [('country', 'country_example'),
                    ('callback', 'param_callback_example'),
                    ('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/history/airquality?postal_code={postal_code}'.format(postal_code=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

