# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameters import CheckNameAvailabilityParameters
from openapi_server.models.check_name_availability_result_resource import CheckNameAvailabilityResultResource


pytestmark = pytest.mark.asyncio

async def test_recovery_services_check_name_availability(client):
    """Test case for recovery_services_check_name_availability

    API to check for resource name availability.  A name is available if no other resource exists that has the same SubscriptionId, Resource Name and Type  or if one or more such resources exist, each of these must be GC'd and their time of deletion be more than 24 Hours Ago
    """
    input = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

