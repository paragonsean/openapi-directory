# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getweatherzipcode200_response import Getweatherzipcode200Response


pytestmark = pytest.mark.asyncio

async def test_getweatherzipcode(client):
    """Test case for getweatherzipcode

    Gets current weather information for a US zip code
    """
    params = [('license', 'license_example'),
                    ('zip', 'zip_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getweatherzipcode',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

