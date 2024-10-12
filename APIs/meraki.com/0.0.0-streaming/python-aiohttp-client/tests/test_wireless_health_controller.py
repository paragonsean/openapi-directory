# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_client_connection_stats(client):
    """Test case for get_network_client_connection_stats

    Aggregated connectivity info for a given client on this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/connectionStats'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_client_latency_stats(client):
    """Test case for get_network_client_latency_stats

    Aggregated latency info for a given client on this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/{client_id}/latencyStats'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_connection_stats(client):
    """Test case for get_network_clients_connection_stats

    Aggregated connectivity info for this network, grouped by clients
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_clients_latency_stats(client):
    """Test case for get_network_clients_latency_stats

    Aggregated latency info for this network, grouped by clients
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/clients/latencyStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_connection_stats(client):
    """Test case for get_network_connection_stats

    Aggregated connectivity info for this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device_connection_stats(client):
    """Test case for get_network_device_connection_stats

    Aggregated connectivity info for a given AP on this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/{serial}/connectionStats'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_device_latency_stats(client):
    """Test case for get_network_device_latency_stats

    Aggregated latency info for a given AP on this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/{serial}/latencyStats'.format(network_id='network_id_example', serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_devices_connection_stats(client):
    """Test case for get_network_devices_connection_stats

    Aggregated connectivity info for this network, grouped by node
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_devices_latency_stats(client):
    """Test case for get_network_devices_latency_stats

    Aggregated latency info for this network, grouped by node
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/devices/latencyStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_failed_connections(client):
    """Test case for get_network_failed_connections

    List of all failed client connection events on this network in a given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('serial', 'serial_example'),
                    ('clientId', 'client_id_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/failedConnections'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_latency_stats(client):
    """Test case for get_network_latency_stats

    Aggregated latency info for this network
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('band', 'band_example'),
                    ('ssid', 56),
                    ('vlan', 56),
                    ('apTag', 'ap_tag_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/latencyStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

