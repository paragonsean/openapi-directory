# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.name_availability import NameAvailability
from openapi_server.models.name_availability_request import NameAvailabilityRequest


pytestmark = pytest.mark.asyncio

async def test_check_name_availability_execute(client):
    """Test case for check_name_availability_execute

    
    """
    name_availability_request = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DBforMySQL/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=name_availability_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

