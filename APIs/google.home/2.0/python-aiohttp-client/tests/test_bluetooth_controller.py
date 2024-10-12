# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_discoverability_request import ChangeDiscoverabilityRequest
from openapi_server.models.example110 import Example110
from openapi_server.models.example111 import Example111
from openapi_server.models.example112 import Example112
from openapi_server.models.forgetpaireddevice_request import ForgetpaireddeviceRequest
from openapi_server.models.pairwith_speaker_request import PairwithSpeakerRequest
from openapi_server.models.scanfordevices_request import ScanfordevicesRequest


pytestmark = pytest.mark.asyncio

async def test_change_discoverability(client):
    """Test case for change_discoverability

    Change Discoverability
    """
    body = {"enable_discovery":True}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/bluetooth/discovery',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forgetpaireddevice(client):
    """Test case for forgetpaireddevice

    Forget paired device
    """
    body = {"bond":False,"mac_address":"xx:xx:xx:xx:xx:xx"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/bluetooth/bond',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_paired_devices(client):
    """Test case for get_paired_devices

    Get Paired Devices
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/bluetooth/get_bonded',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_scan_results(client):
    """Test case for get_scan_results

    Get Scan Results
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/bluetooth/scan_results',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pairwith_speaker(client):
    """Test case for pairwith_speaker

    Pair with Speaker
    """
    body = {"connect":True,"mac_address":"54:13:79:49:19:22","profile":2}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/bluetooth/connect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scanfordevices(client):
    """Test case for scanfordevices

    Scan for devices
    """
    body = {"clear_results":True,"enable":True,"timeout":60}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/bluetooth/scan',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_status(client):
    """Test case for status

    Status
    """
    headers = { 
        'Accept': 'application/json',
        'cast-local-authorization-token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/bluetooth/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

