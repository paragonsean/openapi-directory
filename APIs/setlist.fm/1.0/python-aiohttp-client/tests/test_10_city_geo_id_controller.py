# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_city import JsonCity


pytestmark = pytest.mark.asyncio

async def test_resource10_city_geo_id_get_city_get(client):
    """Test case for resource10_city_geo_id_get_city_get

    Get a city by its unique geoId.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/city/{geo_id}'.format(geo_id='geo_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

