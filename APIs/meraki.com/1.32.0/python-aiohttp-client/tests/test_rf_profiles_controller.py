# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_wireless_rf_profile201_response import CreateNetworkWirelessRfProfile201Response
from openapi_server.models.create_network_wireless_rf_profile_request import CreateNetworkWirelessRfProfileRequest
from openapi_server.models.update_network_wireless_rf_profile_request import UpdateNetworkWirelessRfProfileRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_wireless_rf_profile_1(client):
    """Test case for create_network_wireless_rf_profile_1

    Creates new RF profile for this network
    """
    body = openapi_server.CreateNetworkWirelessRfProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/wireless/rfProfiles'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_wireless_rf_profile_1(client):
    """Test case for delete_network_wireless_rf_profile_1

    Delete a RF Profile
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}'.format(network_id='network_id_example', rf_profile_id='rf_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_rf_profile_1(client):
    """Test case for get_network_wireless_rf_profile_1

    Return a RF profile
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}'.format(network_id='network_id_example', rf_profile_id='rf_profile_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_rf_profiles_1(client):
    """Test case for get_network_wireless_rf_profiles_1

    List the non-basic RF profiles for this network
    """
    params = [('includeTemplateProfiles', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/rfProfiles'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_rf_profile_1(client):
    """Test case for update_network_wireless_rf_profile_1

    Updates specified RF profile for this network
    """
    body = openapi_server.UpdateNetworkWirelessRfProfileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/rfProfiles/{rf_profile_id}'.format(network_id='network_id_example', rf_profile_id='rf_profile_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

