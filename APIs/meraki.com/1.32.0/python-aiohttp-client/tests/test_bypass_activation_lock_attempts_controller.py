# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_sm_bypass_activation_lock_attempt_request import CreateNetworkSmBypassActivationLockAttemptRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_sm_bypass_activation_lock_attempt_1(client):
    """Test case for create_network_sm_bypass_activation_lock_attempt_1

    Bypass activation lock attempt
    """
    body = openapi_server.CreateNetworkSmBypassActivationLockAttemptRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/sm/bypassActivationLockAttempts'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_sm_bypass_activation_lock_attempt_1(client):
    """Test case for get_network_sm_bypass_activation_lock_attempt_1

    Bypass activation lock attempt status
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/sm/bypassActivationLockAttempts/{attempt_id}'.format(network_id='network_id_example', attempt_id='attempt_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

