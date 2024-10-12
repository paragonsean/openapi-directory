# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_get_nearest_relevant_airports(client):
    """Test case for get_nearest_relevant_airports

    Returns a list of relevant airports near to a given point.
    """
    params = [('latitude', 51.57285),
                    ('longitude', -0.44161),
                    ('radius', 500),
                    ('page[limit]', 10),
                    ('page[offset]', 0),
                    ('sort', relevance)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/airports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

