# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_device_loss_and_latency_history_2(client):
    """Test case for get_device_loss_and_latency_history_2

    Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('resolution', 56),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/lossAndLatencyHistory'.format(serial='serial_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

