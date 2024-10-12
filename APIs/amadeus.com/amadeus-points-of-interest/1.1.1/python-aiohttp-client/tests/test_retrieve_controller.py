# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error404 import Error404
from openapi_server.models.error500 import Error500
from openapi_server.models.success1 import Success1


pytestmark = pytest.mark.asyncio

async def test_get_point_of_interest(client):
    """Test case for get_point_of_interest

    Retieve one point of interest by its Id.
    """
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/reference-data/locations/pois/{pois_id}'.format(pois_id='pois_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

