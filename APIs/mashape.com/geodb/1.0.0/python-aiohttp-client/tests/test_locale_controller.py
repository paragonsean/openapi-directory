# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.currencies_response import CurrenciesResponse
from openapi_server.models.date_time_response import DateTimeResponse
from openapi_server.models.forbidden_response import ForbiddenResponse
from openapi_server.models.languages_response import LanguagesResponse
from openapi_server.models.locales_response import LocalesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.time_response import TimeResponse
from openapi_server.models.time_zone_response import TimeZoneResponse
from openapi_server.models.time_zones_response import TimeZonesResponse


pytestmark = pytest.mark.asyncio

async def test_get_currencies_using_get(client):
    """Test case for get_currencies_using_get

    Find currencies
    """
    params = [('countryId', 'country_id_example'),
                    ('hateoasMode', True),
                    ('limit', 10),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/currencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_languages_using_get(client):
    """Test case for get_languages_using_get

    Get languages
    """
    params = [('hateoasMode', True),
                    ('limit', 10),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_locales_using_get(client):
    """Test case for get_locales_using_get

    Get locales
    """
    params = [('hateoasMode', True),
                    ('limit', 10),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/locales',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time_zone_date_time_using_get(client):
    """Test case for get_time_zone_date_time_using_get

    Get time-zone date-time
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/timezones/{zone_id}/dateTime'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time_zone_time_using_get(client):
    """Test case for get_time_zone_time_using_get

    Get time-zone time
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/timezones/{zone_id}/time'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_time_zone_using_get(client):
    """Test case for get_time_zone_using_get

    Get time-zone
    """
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/timezones/{zone_id}'.format(zone_id='zone_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timezones_using_get(client):
    """Test case for get_timezones_using_get

    Get time-zones
    """
    params = [('hateoasMode', True),
                    ('limit', 10),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'UserSecurity': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/locale/timezones',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

