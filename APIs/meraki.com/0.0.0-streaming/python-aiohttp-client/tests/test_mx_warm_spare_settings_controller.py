# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_warm_spare_settings_request import UpdateNetworkWarmSpareSettingsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_warm_spare_settings(client):
    """Test case for get_network_warm_spare_settings

    Return MX warm spare settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/warmSpareSettings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_swap_network_warm_spare(client):
    """Test case for swap_network_warm_spare

    Swap MX primary and warm spare appliances
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/swapWarmSpare'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_warm_spare_settings(client):
    """Test case for update_network_warm_spare_settings

    Update MX warm spare settings
    """
    body = openapi_server.UpdateNetworkWarmSpareSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/warmSpareSettings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

