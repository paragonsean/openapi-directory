# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_pii_sm_devices_for_key_2(client):
    """Test case for get_network_pii_sm_devices_for_key_2

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/pii/smDevicesForKey'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

