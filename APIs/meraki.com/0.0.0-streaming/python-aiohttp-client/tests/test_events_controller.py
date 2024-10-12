# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_events(client):
    """Test case for get_network_events

    List the events for the network
    """
    params = [('productType', 'product_type_example'),
                    ('includedEventTypes', ['included_event_types_example']),
                    ('excludedEventTypes', ['excluded_event_types_example']),
                    ('deviceMac', 'device_mac_example'),
                    ('deviceSerial', 'device_serial_example'),
                    ('deviceName', 'device_name_example'),
                    ('clientIp', 'client_ip_example'),
                    ('clientMac', 'client_mac_example'),
                    ('clientName', 'client_name_example'),
                    ('smDeviceMac', 'sm_device_mac_example'),
                    ('smDeviceName', 'sm_device_name_example'),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/events'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_events_event_types(client):
    """Test case for get_network_events_event_types

    List the event type to human-readable description
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/events/eventTypes'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

