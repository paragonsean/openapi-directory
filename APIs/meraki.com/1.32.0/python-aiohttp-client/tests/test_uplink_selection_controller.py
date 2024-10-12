# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response import GetNetworkApplianceTrafficShapingUplinkSelection200Response
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_selection_request import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_uplink_selection_2(client):
    """Test case for get_network_appliance_traffic_shaping_uplink_selection_2

    Show uplink selection settings for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/uplinkSelection'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_uplink_selection_2(client):
    """Test case for update_network_appliance_traffic_shaping_uplink_selection_2

    Update uplink selection settings for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/uplinkSelection'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

