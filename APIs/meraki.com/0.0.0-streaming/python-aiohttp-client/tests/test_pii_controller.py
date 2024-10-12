# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_pii_request_request import CreateNetworkPiiRequestRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_pii_request(client):
    """Test case for create_network_pii_request

    Submit a new delete or restrict processing PII request
    """
    body = openapi_server.CreateNetworkPiiRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_pii_request(client):
    """Test case for delete_network_pii_request

    Delete a restrict processing PII request
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_pii_keys(client):
    """Test case for get_network_pii_pii_keys

    List the keys required to access Personally Identifiable Information (PII) for a given identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/pii/piiKeys'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_request(client):
    """Test case for get_network_pii_request

    Return a PII request
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/pii/requests/{request_id}'.format(network_id='network_id_example', request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_requests(client):
    """Test case for get_network_pii_requests

    List the PII requests for this network or organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/pii/requests'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_sm_devices_for_key(client):
    """Test case for get_network_pii_sm_devices_for_key

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/pii/smDevicesForKey'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_pii_sm_owners_for_key(client):
    """Test case for get_network_pii_sm_owners_for_key

    Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier
    """
    params = [('username', 'username_example'),
                    ('email', 'email_example'),
                    ('mac', 'mac_example'),
                    ('serial', 'serial_example'),
                    ('imei', 'imei_example'),
                    ('bluetoothMac', 'bluetooth_mac_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/pii/smOwnersForKey'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

