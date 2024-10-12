# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_request import CheckNameAvailabilityRequest
from openapi_server.models.check_name_availability_response import CheckNameAvailabilityResponse


pytestmark = pytest.mark.asyncio

async def test_servers_check_name_availability(client):
    """Test case for servers_check_name_availability

    
    """
    parameters = {"name":"name","type":"Microsoft.Sql/servers"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Sql/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

