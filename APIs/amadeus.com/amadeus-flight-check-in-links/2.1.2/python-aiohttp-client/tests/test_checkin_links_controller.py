# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_get_checkin_urls(client):
    """Test case for get_checkin_urls

    Lists Check-in URLs.
    """
    params = [('airlineCode', 'BA'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v2/reference-data/urls/checkin-links',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

