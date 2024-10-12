# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_sm_devices_fields200_response_inner import UpdateNetworkSmDevicesFields200ResponseInner
from openapi_server.models.update_network_sm_devices_fields_request import UpdateNetworkSmDevicesFieldsRequest


pytestmark = pytest.mark.asyncio

async def test_update_network_sm_devices_fields_2(client):
    """Test case for update_network_sm_devices_fields_2

    Modify the fields of a device
    """
    body = openapi_server.UpdateNetworkSmDevicesFieldsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/sm/devices/fields'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

