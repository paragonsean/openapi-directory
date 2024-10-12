# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcitystandard200_response import Getcitystandard200Response


pytestmark = pytest.mark.asyncio

async def test_getcitystandard(client):
    """Test case for getcitystandard

    Gets a city name standard for US and international cities
    """
    params = [('license', 'license_example'),
                    ('city', 'city_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcitystandard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

