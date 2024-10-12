# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_category_rated_areas200_response import GetCategoryRatedAreas200Response


pytestmark = pytest.mark.asyncio

async def test_get_category_rated_areas(client):
    """Test case for get_category_rated_areas

    GET category rated areas
    """
    params = [('latitude', 41.397158),
                    ('longitude', 2.160873)]
    headers = { 
        'Accept': 'application/vnd.amadeus+json',
    }
    response = await client.request(
        method='GET',
        path='/v1/location/analytics/category-rated-areas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

