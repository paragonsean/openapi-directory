# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.na_healthy_home_coach_data_response import NAHealthyHomeCoachDataResponse


pytestmark = pytest.mark.asyncio

async def test_gethomecoachsdata(client):
    """Test case for gethomecoachsdata

    
    """
    params = [('device_id', 'device_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/gethomecoachsdata',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

