# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_appliance_traffic_shaping_custom_performance_class_request import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.update_network_appliance_traffic_shaping_custom_performance_class_request import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_appliance_traffic_shaping_custom_performance_class_2(client):
    """Test case for create_network_appliance_traffic_shaping_custom_performance_class_2

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

async def test_delete_network_appliance_traffic_shaping_custom_performance_class_2(client):
    """Test case for delete_network_appliance_traffic_shaping_custom_performance_class_2

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

async def test_get_network_appliance_traffic_shaping_custom_performance_class_2(client):
    """Test case for get_network_appliance_traffic_shaping_custom_performance_class_2

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

async def test_get_network_appliance_traffic_shaping_custom_performance_classes_2(client):
    """Test case for get_network_appliance_traffic_shaping_custom_performance_classes_2

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

async def test_update_network_appliance_traffic_shaping_custom_performance_class_2(client):
    """Test case for update_network_appliance_traffic_shaping_custom_performance_class_2

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

