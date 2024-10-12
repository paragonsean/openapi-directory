# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.default_response_dtoof_gym_dto import DefaultResponseDTOOfGymDTO


pytestmark = pytest.mark.asyncio

async def test_gym_get(client):
    """Test case for gym_get

    Get gym details This will return all properties related to gym entity             
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Gym/{gym_id}'.format(gym_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

