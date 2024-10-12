# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success


pytestmark = pytest.mark.asyncio

async def test_get_points_of_interest(client):
    """Test case for get_points_of_interest

    Returns points of interest for a given location and radius.
    """
    params = [('latitude', 41.397158),
                    ('longitude', 2.160873),
                    ('radius', 1),
                    ('page[limit]', 10),
                    ('page[offset]', 0),
                    ('categories', ['categories_example'])]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/pois',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_points_of_interest_by_square(client):
    """Test case for get_points_of_interest_by_square

    Returns points of interest for a given area
    """
    params = [('north', 41.397158),
                    ('west', 2.160873),
                    ('south', 41.394582),
                    ('east', 2.177181),
                    ('page[limit]', 10),
                    ('page[offset]', 0),
                    ('categories', ['categories_example'])]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/pois/by-square',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

