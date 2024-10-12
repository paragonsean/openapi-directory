# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_appliance_traffic_shaping_custom_performance_class_request import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response import GetNetworkApplianceTrafficShapingUplinkBandwidth200Response
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response import GetNetworkApplianceTrafficShapingUplinkSelection200Response
from openapi_server.models.update_network_appliance_traffic_shaping_custom_performance_class_request import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.update_network_appliance_traffic_shaping_request import UpdateNetworkApplianceTrafficShapingRequest
from openapi_server.models.update_network_appliance_traffic_shaping_rules_request import UpdateNetworkApplianceTrafficShapingRulesRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_bandwidth_request import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_selection_request import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_appliance_traffic_shaping_custom_performance_class_1(client):
    """Test case for create_network_appliance_traffic_shaping_custom_performance_class_1

    Add a custom performance class for an MX network
    """
    body = openapi_server.CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_appliance_traffic_shaping_custom_performance_class_1(client):
    """Test case for delete_network_appliance_traffic_shaping_custom_performance_class_1

    Delete a custom performance class from an MX network
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}'.format(network_id='network_id_example', custom_performance_class_id='custom_performance_class_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_1(client):
    """Test case for get_network_appliance_traffic_shaping_1

    Display the traffic shaping settings for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_custom_performance_class_1(client):
    """Test case for get_network_appliance_traffic_shaping_custom_performance_class_1

    Return a custom performance class for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}'.format(network_id='network_id_example', custom_performance_class_id='custom_performance_class_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_custom_performance_classes_1(client):
    """Test case for get_network_appliance_traffic_shaping_custom_performance_classes_1

    List all custom performance classes for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_rules_1(client):
    """Test case for get_network_appliance_traffic_shaping_rules_1

    Display the traffic shaping settings rules for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/rules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_uplink_bandwidth_1(client):
    """Test case for get_network_appliance_traffic_shaping_uplink_bandwidth_1

    Returns the uplink bandwidth limits for your MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/uplinkBandwidth'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_traffic_shaping_uplink_selection_1(client):
    """Test case for get_network_appliance_traffic_shaping_uplink_selection_1

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

async def test_get_network_traffic_shaping_application_categories_1(client):
    """Test case for get_network_traffic_shaping_application_categories_1

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


pytestmark = pytest.mark.asyncio

async def test_get_network_traffic_shaping_dscp_tagging_options_1(client):
    """Test case for get_network_traffic_shaping_dscp_tagging_options_1

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


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_traffic_shaping_rules_2(client):
    """Test case for get_network_wireless_ssid_traffic_shaping_rules_2

    Display the traffic shaping settings for a SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_1(client):
    """Test case for update_network_appliance_traffic_shaping_1

    Update the traffic shaping settings for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceTrafficShapingRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_custom_performance_class_1(client):
    """Test case for update_network_appliance_traffic_shaping_custom_performance_class_1

    Update a custom performance class for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/customPerformanceClasses/{custom_performance_class_id}'.format(network_id='network_id_example', custom_performance_class_id='custom_performance_class_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_rules_1(client):
    """Test case for update_network_appliance_traffic_shaping_rules_1

    Update the traffic shaping settings rules for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceTrafficShapingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/rules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_uplink_bandwidth_1(client):
    """Test case for update_network_appliance_traffic_shaping_uplink_bandwidth_1

    Updates the uplink bandwidth settings for your MX network.
    """
    body = openapi_server.UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/trafficShaping/uplinkBandwidth'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_traffic_shaping_uplink_selection_1(client):
    """Test case for update_network_appliance_traffic_shaping_uplink_selection_1

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


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_traffic_shaping_rules_2(client):
    """Test case for update_network_wireless_ssid_traffic_shaping_rules_2

    Update the traffic shaping settings for an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkWirelessSsidTrafficShapingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

