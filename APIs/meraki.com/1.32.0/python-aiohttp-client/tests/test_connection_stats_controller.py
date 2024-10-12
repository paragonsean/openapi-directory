# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_device_wireless_connection_stats200_response import GetDeviceWirelessConnectionStats200Response
from openapi_server.models.get_network_wireless_connection_stats200_response import GetNetworkWirelessConnectionStats200Response


pytestmark = pytest.mark.asyncio

async def test_get_device_wireless_connection_stats_1(client):
    """Test case for get_device_wireless_connection_stats_1

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
        path='/api/v1/devices/{serial}/wireless/connectionStats'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_client_connection_stats_2(client):
    """Test case for get_network_wireless_client_connection_stats_2

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
        path='/api/v1/networks/{network_id}/wireless/clients/{client_id}/connectionStats'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_clients_connection_stats_2(client):
    """Test case for get_network_wireless_clients_connection_stats_2

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
        path='/api/v1/networks/{network_id}/wireless/clients/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_connection_stats_1(client):
    """Test case for get_network_wireless_connection_stats_1

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
        path='/api/v1/networks/{network_id}/wireless/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_devices_connection_stats_2(client):
    """Test case for get_network_wireless_devices_connection_stats_2

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
        path='/api/v1/networks/{network_id}/wireless/devices/connectionStats'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

