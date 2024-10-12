# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.describetheregionwithin5minutedrive_timeofageographicpoint import Describetheregionwithin5minutedriveTimeofageographicpoint
from openapi_server.models.fetch_administrative_regionsusing_lat_lng import FetchAdministrativeRegionsusingLatLng


pytestmark = pytest.mark.asyncio

async def test_fetch_administrative_regionsusing_lat_lng(client):
    """Test case for fetch_administrative_regionsusing_lat_lng

    Fetch Administrative Regions using Lat/Lng
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/geometries/regions/intersecting/{latitude}/{longitude}'.format(latitude=3.4, longitude=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_geometries(client):
    """Test case for fetch_geometries

    Fetch Geometries
    """
    params = [('location[]', 'location_example')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'x_rapid_api_key': 'x_rapid_api_key_example',
        'x_rapid_api_host': 'x_rapid_api_host_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/geometries/geometry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

