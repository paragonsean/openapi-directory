# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server.models.success1 import Success1


pytestmark = pytest.mark.asyncio

async def test_get_airport_city(client):
    """Test case for get_airport_city

    Returns a specific airports or cities based on its id.
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/{location_id}'.format(location_id='location_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_airport_city_search(client):
    """Test case for get_airport_city_search

    Returns a list of airports and cities matching a given keyword.
    """
    params = [('subType', ['CITY']),
                    ('keyword', 'MUC'),
                    ('countryCode', 'country_code_example'),
                    ('page[limit]', 10),
                    ('page[offset]', 0),
                    ('sort', analytics.travelers.score),
                    ('view', FULL)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

