# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.countries_response import CountriesResponse
from openapi_server.models.country_response import CountryResponse


pytestmark = pytest.mark.asyncio

async def test_countries_get(client):
    """Test case for countries_get

    List of countries
    """
    params = [('page[number]', 56),
                    ('page[size]', 56),
                    ('filter[region]', ['filter_region_example']),
                    ('filter[sub_region]', ['filter_sub_region_example']),
                    ('sort', ['sort_example'])]
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_id_get(client):
    """Test case for countries_id_get

    Country by ID
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

