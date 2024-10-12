# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_device_device_command_logs200_response_inner import GetNetworkSmDeviceDeviceCommandLogs200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_device_command_logs_2(client):
    """Test case for get_network_sm_device_device_command_logs_2

    Return historical records of commands sent to Systems Manager devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/deviceCommandLogs'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

