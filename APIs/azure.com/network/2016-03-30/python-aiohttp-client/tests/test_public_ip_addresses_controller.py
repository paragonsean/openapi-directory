# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.public_ip_address import PublicIPAddress
from openapi_server.models.public_ip_address_list_result import PublicIPAddressListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_public_ip_addresses_create_or_update(client):
    """Test case for public_ip_addresses_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"publicIPAddressVersion":"IPv4","dnsSettings":{"reverseFqdn":"reverseFqdn","fqdn":"fqdn","domainNameLabel":"domainNameLabel"},"ipConfiguration":{"name":"name","etag":"etag","properties":{"subnet":{"name":"name","etag":"etag","properties":{"ipConfigurations":[null,null],"routeTable":{"etag":"etag","properties":{"routes":[{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"addressPrefix":"addressPrefix","nextHopType":"VirtualNetworkGateway","nextHopIpAddress":"nextHopIpAddress","provisioningState":"provisioningState"}}],"subnets":[null,null],"provisioningState":"provisioningState"}},"addressPrefix":"addressPrefix","provisioningState":"provisioningState","networkSecurityGroup":{"etag":"etag","properties":{"defaultSecurityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"networkInterfaces":[{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}},{"etag":"etag","properties":{"ipConfigurations":[null,null],"virtualMachine":{"id":"id"},"macAddress":"macAddress","dnsSettings":{"appliedDnsServers":["appliedDnsServers","appliedDnsServers"],"internalDnsNameLabel":"internalDnsNameLabel","internalDomainNameSuffix":"internalDomainNameSuffix","internalFqdn":"internalFqdn","dnsServers":["dnsServers","dnsServers"]},"resourceGuid":"resourceGuid","provisioningState":"provisioningState","enableIPForwarding":True,"primary":True}}],"resourceGuid":"resourceGuid","securityRules":[{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}},{"name":"name","etag":"etag","properties":{"destinationAddressPrefix":"destinationAddressPrefix","protocol":"Tcp","access":"Allow","sourcePortRange":"sourcePortRange","sourceAddressPrefix":"sourceAddressPrefix","destinationPortRange":"destinationPortRange","description":"description","provisioningState":"provisioningState","priority":5,"direction":"Inbound"}}],"subnets":[null,null],"provisioningState":"provisioningState"}}}},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState"}},"resourceGuid":"resourceGuid","idleTimeoutInMinutes":5,"ipAddress":"ipAddress","provisioningState":"provisioningState","publicIPAllocationMethod":"Static"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}'.format(resource_group_name='resource_group_name_example', public_ip_address_name='public_ip_address_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_delete(client):
    """Test case for public_ip_addresses_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}'.format(resource_group_name='resource_group_name_example', public_ip_address_name='public_ip_address_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_get(client):
    """Test case for public_ip_addresses_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses/{public_ip_address_name}'.format(resource_group_name='resource_group_name_example', public_ip_address_name='public_ip_address_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_list(client):
    """Test case for public_ip_addresses_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPAddresses'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_addresses_list_all(client):
    """Test case for public_ip_addresses_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/publicIPAddresses'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

