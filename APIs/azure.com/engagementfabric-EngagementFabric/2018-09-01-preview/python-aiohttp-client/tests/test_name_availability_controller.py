# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_parameter import CheckNameAvailabilityParameter
from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_check_name_availability(client):
    """Test case for check_name_availability

    Check availability of EngagementFabric resource
    """
    parameters = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.EngagementFabric/checkNameAvailability'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

