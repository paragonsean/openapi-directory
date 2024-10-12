# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_device_cellular_usage_history200_response_inner import GetNetworkSmDeviceCellularUsageHistory200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_cellular_usage_history_2(client):
    """Test case for get_network_sm_device_cellular_usage_history_2

    Return the client's daily cellular data usage history
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/cellularUsageHistory'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

