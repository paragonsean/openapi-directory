# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_shaping_dscp_tagging_options_2(client):
    """Test case for get_network_traffic_shaping_dscp_tagging_options_2

    Returns the available DSCP tagging options for your traffic shaping rules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/trafficShaping/dscpTaggingOptions'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

