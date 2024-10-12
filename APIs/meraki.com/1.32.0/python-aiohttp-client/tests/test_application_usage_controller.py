# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_clients_application_usage_2(client):
    """Test case for get_network_clients_application_usage_2

    Return the application usage data for clients
    """
    params = [('clients', 'clients_example'),
                    ('ssidNumber', 56),
                    ('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/clients/applicationUsage'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

