# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_countries import JsonCountries


pytestmark = pytest.mark.asyncio

async def test_resource10_search_countries_get_countries_get(client):
    """Test case for resource10_search_countries_get_countries_get

    Get a complete list of all supported countries.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/search/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

