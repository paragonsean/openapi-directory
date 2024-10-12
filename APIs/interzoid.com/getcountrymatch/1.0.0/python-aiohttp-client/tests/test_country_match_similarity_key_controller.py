# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcountrymatch200_response import Getcountrymatch200Response


pytestmark = pytest.mark.asyncio

async def test_getcountrymatch(client):
    """Test case for getcountrymatch

    Gets a similarity key for matching purposes for country name data
    """
    params = [('license', 'license_example'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/getcountrymatch',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

