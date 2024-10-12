# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_wireless_ssid_eap_override200_response import GetNetworkWirelessSsidEapOverride200Response
from openapi_server.models.update_network_wireless_ssid_eap_override_request import UpdateNetworkWirelessSsidEapOverrideRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_eap_override_2(client):
    """Test case for get_network_wireless_ssid_eap_override_2

    Return the EAP overridden parameters for an SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/eapOverride'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_eap_override_2(client):
    """Test case for update_network_wireless_ssid_eap_override_2

    Update the EAP overridden parameters for an SSID.
    """
    body = openapi_server.UpdateNetworkWirelessSsidEapOverrideRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/eapOverride'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

