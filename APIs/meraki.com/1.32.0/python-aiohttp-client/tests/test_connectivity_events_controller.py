# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_client_connectivity_events_2(client):
    """Test case for get_network_wireless_client_connectivity_events_2

    List the wireless connectivity events for a client within a network in the timespan.
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('types', ['types_example']),
                    ('includedSeverities', ['included_severities_example']),
                    ('band', 'band_example'),
                    ('ssidNumber', 56),
                    ('deviceSerial', 'device_serial_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/clients/{client_id}/connectivityEvents'.format(network_id='network_id_example', client_id='client_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

