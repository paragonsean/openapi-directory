# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_clients200_response import GetNetworkClients200Response
from openapi_server.models.provision_network_clients_request import ProvisionNetworkClientsRequest
from openapi_server.models.update_network_client_policy_request import UpdateNetworkClientPolicyRequest
from openapi_server.models.update_network_client_splash_authorization_status_request import UpdateNetworkClientSplashAuthorizationStatusRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_clients(client):
    """Test case for get_device_clients

    List the clients of a device, up to a maximum of a month ago
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/devices/{serial}/clients'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client(client):
    """Test case for get_network_client

    Return the client associated with the given identifier
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_events(client):
    """Test case for get_network_client_events

    Return the events associated with this client
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/events'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_latency_history(client):
    """Test case for get_network_client_latency_history

    Return the latency history for a client
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/latencyHistory'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_policy(client):
    """Test case for get_network_client_policy

    Return the policy assigned to a client on the network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_splash_authorization_status(client):
    """Test case for get_network_client_splash_authorization_status

    Return the splash authorization for a client, for each SSID they've associated with through splash
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_usage_history(client):
    """Test case for get_network_client_usage_history

    Return the client's daily usage history
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/usageHistory'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients(client):
    """Test case for get_network_clients

    List the clients that have used this network in the timespan
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provision_network_clients(client):
    """Test case for provision_network_clients

    Provisions a client with a name and policy
    """
    body = openapi_server.ProvisionNetworkClientsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/clients/provision'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_policy(client):
    """Test case for update_network_client_policy

    Update the policy assigned to a client on the network
    """
    body = openapi_server.UpdateNetworkClientPolicyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/clients/{client_id}/policy'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_client_splash_authorization_status(client):
    """Test case for update_network_client_splash_authorization_status

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
        path='/api/v0/networks/{network_id}/clients/{client_id}/splashAuthorizationStatus'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

