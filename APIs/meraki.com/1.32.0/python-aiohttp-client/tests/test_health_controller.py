# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_health_alerts200_response_inner import GetNetworkHealthAlerts200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_network_health_alerts_1(client):
    """Test case for get_network_health_alerts_1

    Return all global alerts on this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/health/alerts'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

