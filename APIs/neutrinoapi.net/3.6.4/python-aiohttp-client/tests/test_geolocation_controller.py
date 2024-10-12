# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.geocode_address_response import GeocodeAddressResponse
from openapi_server.models.geocode_reverse_response import GeocodeReverseResponse
from openapi_server.models.ip_info_response import IPInfoResponse


pytestmark = pytest.mark.asyncio

async def test_geocode_address(client):
    """Test case for geocode_address

    Geocode Address
    """
    params = [('address', 'address_example'),
                    ('house-number', 'house_number_example'),
                    ('street', 'street_example'),
                    ('city', 'city_example'),
                    ('county', 'county_example'),
                    ('state', 'state_example'),
                    ('postal-code', 'postal_code_example'),
                    ('country-code', 'country_code_example'),
                    ('language-code', 'en'),
                    ('fuzzy-search', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/geocode-address',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geocode_reverse(client):
    """Test case for geocode_reverse

    Geocode Reverse
    """
    params = [('latitude', 'latitude_example'),
                    ('longitude', 'longitude_example'),
                    ('language-code', 'en'),
                    ('zoom', 'address')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/geocode-reverse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_i_p_info(client):
    """Test case for i_p_info

    IP Info
    """
    params = [('ip', 'ip_example'),
                    ('reverse-lookup', False)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
        'user-id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ip-info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

