# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cities_city_id_get200_response import CitiesCityIdGet200Response
from openapi_server.models.cities_get200_response import CitiesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_cities_city_id_get(client):
    """Test case for cities_city_id_get

    Get details about one city
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cities/{city_id}'.format(city_id='city_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_get(client):
    """Test case for cities_get

    Get list of cities supported in Apacta
    """
    params = [('zip_code', 'zip_code_example'),
                    ('name', 'name_example'),
                    ('include_all', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

