# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getweather200_response import Getweather200Response


pytestmark = pytest.mark.asyncio

async def test_getweather(client):
    """Test case for getweather

    Gets current weather information for a US city and state
    """
    params = [('license', 'license_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getweather',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

