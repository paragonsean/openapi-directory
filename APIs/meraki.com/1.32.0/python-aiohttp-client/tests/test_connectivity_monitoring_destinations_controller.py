# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_network_appliance_connectivity_monitoring_destinations_request import UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest
from openapi_server.models.update_network_cellular_gateway_connectivity_monitoring_destinations_request import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_connectivity_monitoring_destinations_1(client):
    """Test case for get_network_appliance_connectivity_monitoring_destinations_1

    Return the connectivity testing destinations for an MX network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/connectivityMonitoringDestinations'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_gateway_connectivity_monitoring_destinations_1(client):
    """Test case for get_network_cellular_gateway_connectivity_monitoring_destinations_1

    Return the connectivity testing destinations for an MG network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/connectivityMonitoringDestinations'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_connectivity_monitoring_destinations_1(client):
    """Test case for update_network_appliance_connectivity_monitoring_destinations_1

    Update the connectivity testing destinations for an MX network
    """
    body = openapi_server.UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/connectivityMonitoringDestinations'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_connectivity_monitoring_destinations_1(client):
    """Test case for update_network_cellular_gateway_connectivity_monitoring_destinations_1

    Update the connectivity testing destinations for an MG network
    """
    body = openapi_server.UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/connectivityMonitoringDestinations'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

