# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult


pytestmark = pytest.mark.asyncio

async def test_storage_sync_services_check_name_availability(client):
    """Test case for storage_sync_services_check_name_availability

    
    """
    parameters = {"name":"name","type":"Microsoft.StorageSync/storageSyncServices"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.StorageSync/locations/{location_name}/checkNameAvailability'.format(location_name='location_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

