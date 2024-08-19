# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.countries_list import CountriesList


pytestmark = pytest.mark.asyncio

async def test_v3_countries_get(client):
    """Test case for v3_countries_get

    Gets countries codes and names.
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

