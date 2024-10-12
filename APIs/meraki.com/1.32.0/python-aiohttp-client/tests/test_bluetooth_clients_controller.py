# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_bluetooth_client_1(client):
    """Test case for get_network_bluetooth_client_1

    Return a Bluetooth client
    """
    params = [('includeConnectivityHistory', True),
                    ('connectivityHistoryTimespan', 56)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/bluetoothClients/{bluetooth_client_id}'.format(network_id='network_id_example', bluetooth_client_id='bluetooth_client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_bluetooth_clients_1(client):
    """Test case for get_network_bluetooth_clients_1

    List the Bluetooth clients seen by APs in this network
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('includeConnectivityHistory', True)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/bluetoothClients'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

