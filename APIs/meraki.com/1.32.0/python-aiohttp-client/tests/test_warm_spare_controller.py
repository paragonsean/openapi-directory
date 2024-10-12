# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_device_switch_warm_spare_request import UpdateDeviceSwitchWarmSpareRequest
from openapi_server.models.update_network_appliance_warm_spare_request import UpdateNetworkApplianceWarmSpareRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_switch_warm_spare_1(client):
    """Test case for get_device_switch_warm_spare_1

    Return warm spare configuration for a switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/switch/warmSpare'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_warm_spare_1(client):
    """Test case for get_network_appliance_warm_spare_1

    Return MX warm spare settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/warmSpare'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_swap_network_appliance_warm_spare_1(client):
    """Test case for swap_network_appliance_warm_spare_1

    Swap MX primary and warm spare appliances
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/appliance/warmSpare/swap'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_switch_warm_spare_1(client):
    """Test case for update_device_switch_warm_spare_1

    Update warm spare configuration for a switch
    """
    body = openapi_server.UpdateDeviceSwitchWarmSpareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/switch/warmSpare'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_warm_spare_1(client):
    """Test case for update_network_appliance_warm_spare_1

    Update MX warm spare settings
    """
    body = openapi_server.UpdateNetworkApplianceWarmSpareRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/warmSpare'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

