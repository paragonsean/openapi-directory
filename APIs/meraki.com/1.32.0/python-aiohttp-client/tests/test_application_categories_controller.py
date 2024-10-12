# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_firewall_l7_firewall_rules_application_categories_3(client):
    """Test case for get_network_appliance_firewall_l7_firewall_rules_application_categories_3

    Return the L7 firewall application categories and their associated applications for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/firewall/l7FirewallRules/applicationCategories'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_shaping_application_categories_2(client):
    """Test case for get_network_traffic_shaping_application_categories_2

    Returns the application categories for traffic shaping rules.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/trafficShaping/applicationCategories'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

