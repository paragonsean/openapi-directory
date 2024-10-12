# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bng2latlong_easting_northing_get200_response import Bng2latlongEastingNorthingGet200Response


pytestmark = pytest.mark.asyncio

async def test_bng2latlong_easting_northing_get(client):
    """Test case for bng2latlong_easting_northing_get

    Returns latitude and longitude for the given easting and northing.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/bng2latlong/{easting}/{northing}'.format(easting=326897, northing=673919),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

