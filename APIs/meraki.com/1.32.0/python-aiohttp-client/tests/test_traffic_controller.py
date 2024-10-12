# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_1(client):
    """Test case for get_network_traffic_1

    Return the traffic analysis data for this network
    """
    params = [('t0', 't0_example'),
                    ('timespan', 3.4),
                    ('deviceType', 'device_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/traffic'.format(network_id='network_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

