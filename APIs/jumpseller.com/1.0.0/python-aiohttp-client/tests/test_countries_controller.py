# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.not_found import NotFound
from openapi_server.models.region import Region


pytestmark = pytest.mark.asyncio

async def test_countries_country_code_json_get(client):
    """Test case for countries_country_code_json_get

    Retrieve a single Country information.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{country_code_jso}'.format(country_code='country_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_country_code_regions_json_get(client):
    """Test case for countries_country_code_regions_json_get

    Retrieve all Regions from a single Country.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{country_code}/regions.json'.format(country_code='country_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_country_code_regions_region_code_json_get(client):
    """Test case for countries_country_code_regions_region_code_json_get

    Retrieve a single Region information object.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{country_code}/regions/{region_code_jso}'.format(country_code='country_code_example', region_code='region_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_json_get(client):
    """Test case for countries_json_get

    Retrieve all Countries.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

