# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response import ApiResponse


pytestmark = pytest.mark.asyncio

async def test_wgs84_to_osgb36_using_get(client):
    """Test case for wgs84_to_osgb36_using_get

    wgs84ToOsgb36
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v1/wgs84ToOsgb36/{latitude}/{longitude}'.format(latitude='latitude_example', longitude='longitude_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

