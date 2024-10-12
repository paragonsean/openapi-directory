# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_input import CheckNameAvailabilityInput
from openapi_server.models.check_name_availability_output import CheckNameAvailabilityOutput
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_check_front_door_name_availability_with_subscription(client):
    """Test case for check_front_door_name_availability_with_subscription

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/checkFrontDoorNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=check_front_door_name_availability_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

