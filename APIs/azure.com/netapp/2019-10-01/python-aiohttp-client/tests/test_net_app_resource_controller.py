# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.resource_name_availability import ResourceNameAvailability
from openapi_server.models.resource_name_availability_request import ResourceNameAvailabilityRequest


pytestmark = pytest.mark.asyncio

async def test_net_app_resource_check_file_path_availability(client):
    """Test case for net_app_resource_check_file_path_availability

    Check file path availability
    """
    body = {"resourceGroup":"resourceGroup","name":"name","type":"Microsoft.NetApp/netAppAccounts"}
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.NetApp/locations/{location}/checkFilePathAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_net_app_resource_check_name_availability(client):
    """Test case for net_app_resource_check_name_availability

    Check resource name availability
    """
    body = {"resourceGroup":"resourceGroup","name":"name","type":"Microsoft.NetApp/netAppAccounts"}
    params = [('api-version', '2019-10-01')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.NetApp/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

