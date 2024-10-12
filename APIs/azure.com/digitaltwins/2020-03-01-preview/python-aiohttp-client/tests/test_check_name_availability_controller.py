# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_request import CheckNameRequest
from openapi_server.models.check_name_result import CheckNameResult
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_digital_twins_check_name_availability(client):
    """Test case for digital_twins_check_name_availability

    
    """
    digital_twins_instance_check_name = {"name":"name","type":"Microsoft.DigitalTwins/digitalTwinsInstances"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DigitalTwins/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=digital_twins_instance_check_name,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

