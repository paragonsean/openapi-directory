# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_list_result import VirtualNetworkListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_networks_create_or_update(client):
    """Test case for virtual_networks_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"resourceGuid":"resourceGuid","addressSpace":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"dhcpOptions":{"dnsServers":["dnsServers","dnsServers"]},"VirtualNetworkPeerings":[{"name":"name","etag":"etag","properties":{"remoteVirtualNetwork":{"id":"id"},"allowVirtualNetworkAccess":True,"peeringState":"Initiated","allowGatewayTransit":True,"provisioningState":"provisioningState","allowForwardedTraffic":True,"useRemoteGateways":True}},{"name":"name","etag":"etag","properties":{"remoteVirtualNetwork":{"id":"id"},"allowVirtualNetworkAccess":True,"peeringState":"Initiated","allowGatewayTransit":True,"provisioningState":"provisioningState","allowForwardedTraffic":True,"useRemoteGateways":True}}],"subnets":[{"name":"name","etag":"etag","properties":{"ipConfigurations":[null,null],"resourceNavigationLinks":[{"name":"name","etag":"etag","properties":{"link":"link","linkedResourceType":"linkedResourceType","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"link":"link","linkedResourceType":"linkedResourceType","provisioningState":"provisioningState"}}],"routeTable":{"etag":"etag","properties":{"routes":[{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}}],"subnets":[null,null],"provisioningState":"provisioningState"}},"addressPrefix":"addressPrefix","provisioningState":"provisioningState","networkSecurityGroup":{"etag":"etag","properties":{"defaultSecurityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"networkInterfaces":[{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}},{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}}],"resourceGuid":"resourceGuid","securityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"subnets":[null,null],"provisioningState":"provisioningState"}}}},{"name":"name","etag":"etag","properties":{"ipConfigurations":[null,null],"resourceNavigationLinks":[{"name":"name","etag":"etag","properties":{"link":"link","linkedResourceType":"linkedResourceType","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"link":"link","linkedResourceType":"linkedResourceType","provisioningState":"provisioningState"}}],"routeTable":{"etag":"etag","properties":{"routes":[{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}}],"subnets":[null,null],"provisioningState":"provisioningState"}},"addressPrefix":"addressPrefix","provisioningState":"provisioningState","networkSecurityGroup":{"etag":"etag","properties":{"defaultSecurityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"networkInterfaces":[{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}},{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}}],"resourceGuid":"resourceGuid","securityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"subnets":[null,null],"provisioningState":"provisioningState"}}}}],"provisioningState":"provisioningState"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_delete(client):
    """Test case for virtual_networks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_get(client):
    """Test case for virtual_networks_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks/{virtual_network_name}'.format(resource_group_name='resource_group_name_example', virtual_network_name='virtual_network_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_list(client):
    """Test case for virtual_networks_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworks'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_networks_list_all(client):
    """Test case for virtual_networks_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/virtualNetworks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

