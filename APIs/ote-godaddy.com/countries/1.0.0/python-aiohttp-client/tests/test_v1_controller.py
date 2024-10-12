# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.country import Country
from openapi_server.models.country_summary import CountrySummary
from openapi_server.models.error import Error
from openapi_server.models.error_limit import ErrorLimit


pytestmark = pytest.mark.asyncio

async def test_get_countries(client):
    """Test case for get_countries

    Retrieves summary country information for the provided marketId and filters
    """
    params = [('marketId', 'market_id_example'),
                    ('regionTypeId', 56),
                    ('regionName', 'region_name_example'),
                    ('sort', key),
                    ('order', ascending)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_country(client):
    """Test case for get_country

    Retrieves country and summary state information for provided countryKey
    """
    params = [('marketId', 'market_id_example'),
                    ('sort', key),
                    ('order', ascending)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/countries/{country_key}'.format(country_key='country_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

