# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_wireless_ssid_identity_psk_request import CreateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.get_network_wireless_ssid_identity_psks200_response_inner import GetNetworkWirelessSsidIdentityPsks200ResponseInner
from openapi_server.models.update_network_wireless_ssid_identity_psk_request import UpdateNetworkWirelessSsidIdentityPskRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_wireless_ssid_identity_psk_2(client):
    """Test case for create_network_wireless_ssid_identity_psk_2

    Create an Identity PSK
    """
    body = openapi_server.CreateNetworkWirelessSsidIdentityPskRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_wireless_ssid_identity_psk_2(client):
    """Test case for delete_network_wireless_ssid_identity_psk_2

    Delete an Identity PSK
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_identity_psk_2(client):
    """Test case for get_network_wireless_ssid_identity_psk_2

    Return an Identity PSK
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_identity_psks_2(client):
    """Test case for get_network_wireless_ssid_identity_psks_2

    List all Identity PSKs in a wireless network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_identity_psk_2(client):
    """Test case for update_network_wireless_ssid_identity_psk_2

    Update an Identity PSK
    """
    body = openapi_server.UpdateNetworkWirelessSsidIdentityPskRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

