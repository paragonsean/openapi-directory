# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_client_splash_authorization_status_2(client):
    """Test case for get_network_client_splash_authorization_status_2

    Return the splash authorization for a client, for each SSID they've associated with through splash
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_splash_authorization_status_2(client):
    """Test case for update_network_client_splash_authorization_status_2

    Update a client's splash authorization
    """
    body = openapi_server.UpdateNetworkClientSplashAuthorizationStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

