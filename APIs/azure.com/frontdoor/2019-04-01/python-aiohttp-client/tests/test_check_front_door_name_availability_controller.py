# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_check_front_door_name_availability(client):
    """Test case for check_front_door_name_availability

    
    """
    check_front_door_name_availability_input = {"name":"name","type":"Microsoft.Network/frontDoors"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Network/checkFrontDoorNameAvailability',
        headers=headers,
        json=check_front_door_name_availability_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

