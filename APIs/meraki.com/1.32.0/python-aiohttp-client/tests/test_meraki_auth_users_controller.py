# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_meraki_auth_user_request import CreateNetworkMerakiAuthUserRequest
from openapi_server.models.get_network_meraki_auth_users200_response_inner import GetNetworkMerakiAuthUsers200ResponseInner
from openapi_server.models.update_network_meraki_auth_user_request import UpdateNetworkMerakiAuthUserRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_meraki_auth_user_1(client):
    """Test case for create_network_meraki_auth_user_1

    Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)
    """
    body = openapi_server.CreateNetworkMerakiAuthUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/merakiAuthUsers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_meraki_auth_user_1(client):
    """Test case for delete_network_meraki_auth_user_1

    Deauthorize a user
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_user_1(client):
    """Test case for get_network_meraki_auth_user_1

    Return the Meraki Auth splash guest, RADIUS, or client VPN user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_users_1(client):
    """Test case for get_network_meraki_auth_users_1

    List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/merakiAuthUsers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_meraki_auth_user_1(client):
    """Test case for update_network_meraki_auth_user_1

    Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)
    """
    body = openapi_server.UpdateNetworkMerakiAuthUserRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

