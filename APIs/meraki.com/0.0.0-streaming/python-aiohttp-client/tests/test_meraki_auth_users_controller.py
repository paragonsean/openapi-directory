# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_user(client):
    """Test case for get_network_meraki_auth_user

    Return the Meraki Auth splash or RADIUS user
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/merakiAuthUsers/{meraki_auth_user_id}'.format(network_id='network_id_example', meraki_auth_user_id='meraki_auth_user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_meraki_auth_users(client):
    """Test case for get_network_meraki_auth_users

    List the splash or RADIUS users configured under Meraki Authentication for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/merakiAuthUsers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

