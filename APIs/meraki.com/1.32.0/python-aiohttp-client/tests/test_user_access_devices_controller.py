# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_sm_user_access_devices200_response_inner import GetNetworkSmUserAccessDevices200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_delete_network_sm_user_access_device_1(client):
    """Test case for delete_network_sm_user_access_device_1

    Delete a User Access Device
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/sm/userAccessDevices/{user_access_device_id}'.format(network_id='network_id_example', user_access_device_id='user_access_device_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_user_access_devices_1(client):
    """Test case for get_network_sm_user_access_devices_1

    List User Access Devices and its Trusted Access Connections
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
        path='/api/v1/networks/{network_id}/sm/userAccessDevices'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

