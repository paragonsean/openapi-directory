# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.countries_country_id_get200_response import CountriesCountryIdGet200Response
from openapi_server.models.countries_get200_response import CountriesGet200Response
from openapi_server.models.error_not_found import ErrorNotFound


pytestmark = pytest.mark.asyncio

async def test_countries_country_id_get(client):
    """Test case for countries_country_id_get

    Get details about one country
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/countries/{country_id}'.format(country_id='country_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_get(client):
    """Test case for countries_get

    Get list of countries supported in Apacta
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

