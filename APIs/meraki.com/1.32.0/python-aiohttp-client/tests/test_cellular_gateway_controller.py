# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_cellular_gateway_dhcp200_response import GetNetworkCellularGatewayDhcp200Response
from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.update_device_cellular_gateway_lan_request import UpdateDeviceCellularGatewayLanRequest
from openapi_server.models.update_device_cellular_gateway_port_forwarding_rules_request import UpdateDeviceCellularGatewayPortForwardingRulesRequest
from openapi_server.models.update_network_cellular_gateway_connectivity_monitoring_destinations_request import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest
from openapi_server.models.update_network_cellular_gateway_dhcp_request import UpdateNetworkCellularGatewayDhcpRequest
from openapi_server.models.update_network_cellular_gateway_subnet_pool_request import UpdateNetworkCellularGatewaySubnetPoolRequest
from openapi_server.models.update_network_cellular_gateway_uplink_request import UpdateNetworkCellularGatewayUplinkRequest


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_gateway_lan(client):
    """Test case for get_device_cellular_gateway_lan

    Show the LAN Settings of a MG
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellularGateway/lan'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_device_cellular_gateway_port_forwarding_rules(client):
    """Test case for get_device_cellular_gateway_port_forwarding_rules

    Returns the port forwarding rules for a single MG.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/devices/{serial}/cellularGateway/portForwardingRules'.format(serial='serial_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_gateway_connectivity_monitoring_destinations(client):
    """Test case for get_network_cellular_gateway_connectivity_monitoring_destinations

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

async def test_get_network_cellular_gateway_dhcp(client):
    """Test case for get_network_cellular_gateway_dhcp

    List common DHCP settings of MGs
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/dhcp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_gateway_subnet_pool(client):
    """Test case for get_network_cellular_gateway_subnet_pool

    Return the subnet pool and mask configured for MGs in the network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/subnetPool'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_cellular_gateway_uplink(client):
    """Test case for get_network_cellular_gateway_uplink

    Returns the uplink settings for your MG network.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/cellularGateway/uplink'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_cellular_gateway_uplink_statuses(client):
    """Test case for get_organization_cellular_gateway_uplink_statuses

    List the uplink status of every Meraki MG cellular gateway in the organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('serials', ['serials_example']),
                    ('iccids', ['iccids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/cellularGateway/uplink/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_gateway_lan(client):
    """Test case for update_device_cellular_gateway_lan

    Update the LAN Settings for a single MG.
    """
    body = openapi_server.UpdateDeviceCellularGatewayLanRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellularGateway/lan'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_device_cellular_gateway_port_forwarding_rules(client):
    """Test case for update_device_cellular_gateway_port_forwarding_rules

    Updates the port forwarding rules for a single MG.
    """
    body = openapi_server.UpdateDeviceCellularGatewayPortForwardingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/devices/{serial}/cellularGateway/portForwardingRules'.format(serial='serial_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_connectivity_monitoring_destinations(client):
    """Test case for update_network_cellular_gateway_connectivity_monitoring_destinations

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


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_dhcp(client):
    """Test case for update_network_cellular_gateway_dhcp

    Update common DHCP settings of MGs
    """
    body = openapi_server.UpdateNetworkCellularGatewayDhcpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/dhcp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_subnet_pool(client):
    """Test case for update_network_cellular_gateway_subnet_pool

    Update the subnet pool and mask configuration for MGs in the network.
    """
    body = openapi_server.UpdateNetworkCellularGatewaySubnetPoolRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/subnetPool'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_cellular_gateway_uplink(client):
    """Test case for update_network_cellular_gateway_uplink

    Updates the uplink settings for your MG network.
    """
    body = openapi_server.UpdateNetworkCellularGatewayUplinkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/cellularGateway/uplink'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

