# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_service_check_name_availability_parameters import DeviceServiceCheckNameAvailabilityParameters
from openapi_server.models.device_service_name_availability_info import DeviceServiceNameAvailabilityInfo
from openapi_server.models.error_details import ErrorDetails


pytestmark = pytest.mark.asyncio

async def test_services_check_device_service_name_availability(client):
    """Test case for services_check_device_service_name_availability

    
    """
    device_service_check_name_availability_parameters = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.WindowsIoT/checkDeviceServiceNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=device_service_check_name_availability_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

