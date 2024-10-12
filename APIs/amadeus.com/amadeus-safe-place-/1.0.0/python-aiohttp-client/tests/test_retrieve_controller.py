# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success1 import Success1


pytestmark = pytest.mark.asyncio

async def test_get_location_safety_ranking(client):
    """Test case for get_location_safety_ranking

    Retieve safety information of a location by its Id.
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/safety/safety-rated-locations/{safety_rated_location_id}'.format(safety_rated_location_id='safety_rated_location_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

