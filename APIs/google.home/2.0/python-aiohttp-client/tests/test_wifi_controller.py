# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connectto_wi_fi_network_request import ConnecttoWiFiNetworkRequest
from openapi_server.models.example113 import Example113
from openapi_server.models.example114 import Example114
from openapi_server.models.forget_wi_fi_network_request import ForgetWiFiNetworkRequest


pytestmark = pytest.mark.asyncio

async def test_connectto_wi_fi_network(client):
    """Test case for connectto_wi_fi_network

    Connect to Wi-Fi Network
    """
    body = {"bssid":"5c:0a:xx:xx:xx:xx","enc_passwd":"xxxxxfPY=","signal_level":-42,"ssid":"myotherssid","wpa_auth":7,"wpa_cipher":4}
    headers = { 
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/connect_wifi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forget_wi_fi_network(client):
    """Test case for forget_wi_fi_network

    Forget Wi-Fi Network
    """
    body = {"wpa_id":0}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/forget_wifi',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saved_networks(client):
    """Test case for get_saved_networks

    Get Saved Networks
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/configured_networks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wi_fi_scan_results(client):
    """Test case for get_wi_fi_scan_results

    Get Wi-Fi Scan Results
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/scan_results',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scanfor_networks(client):
    """Test case for scanfor_networks

    Scan for Networks
    """
    headers = { 
        'Accept': 'text/plain',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/scan_wifi',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

