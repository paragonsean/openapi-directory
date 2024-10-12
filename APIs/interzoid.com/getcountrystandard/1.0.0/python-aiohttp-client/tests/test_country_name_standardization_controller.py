# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcountrystandard200_response import Getcountrystandard200Response


pytestmark = pytest.mark.asyncio

async def test_getcountrystandard(client):
    """Test case for getcountrystandard

    Gets country name standard
    """
    params = [('license', 'license_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcountrystandard',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

