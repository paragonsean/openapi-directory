# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcitymatch200_response import Getcitymatch200Response


pytestmark = pytest.mark.asyncio

async def test_getcitymatch(client):
    """Test case for getcitymatch

    Gets a similarity key for matching purposes for city name data
    """
    params = [('license', 'license_example'),
                    ('city', 'city_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcitymatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

