# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_pii_pii_keys_2(client):
    """Test case for get_network_pii_pii_keys_2

    List the keys required to access Personally Identifiable Information (PII) for a given identifier
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
        path='/api/v1/networks/{network_id}/pii/piiKeys'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

