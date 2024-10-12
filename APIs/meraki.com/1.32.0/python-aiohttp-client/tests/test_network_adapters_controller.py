# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_device_network_adapters200_response_inner import GetNetworkSmDeviceNetworkAdapters200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_device_network_adapters_2(client):
    """Test case for get_network_sm_device_network_adapters_2

    List the network adapters of a device
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/devices/{device_id}/networkAdapters'.format(network_id='network_id_example', device_id='device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

