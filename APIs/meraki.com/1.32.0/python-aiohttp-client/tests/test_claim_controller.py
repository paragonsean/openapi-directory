# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest


pytestmark = pytest.mark.asyncio

async def test_vmx_network_devices_claim_2(client):
    """Test case for vmx_network_devices_claim_2

    Claim a vMX into a network
    """
    body = openapi_server.VmxNetworkDevicesClaimRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/devices/claim/vmx'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

