# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.azure_firewall import AzureFirewall
from openapi_server.models.azure_firewall_list_result import AzureFirewallListResult


pytestmark = pytest.mark.asyncio

async def test_azure_firewalls_create_or_update(client):
    """Test case for azure_firewalls_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAddress":"privateIPAddress","internalPublicIpAddress":{"id":"id"},"publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAddress":"privateIPAddress","internalPublicIpAddress":{"id":"id"},"publicIPAddress":{"id":"id"}}}],"networkRuleCollections":[{"name":"name","etag":"etag","properties":{"action":{"type":"Allow"},"rules":[{"sourceAddresses":["sourceAddresses","sourceAddresses"],"destinationPorts":["destinationPorts","destinationPorts"],"name":"name","description":"description","destinationAddresses":["destinationAddresses","destinationAddresses"],"protocols":["TCP","TCP"]},{"sourceAddresses":["sourceAddresses","sourceAddresses"],"destinationPorts":["destinationPorts","destinationPorts"],"name":"name","description":"description","destinationAddresses":["destinationAddresses","destinationAddresses"],"protocols":["TCP","TCP"]}],"priority":9613}},{"name":"name","etag":"etag","properties":{"action":{"type":"Allow"},"rules":[{"sourceAddresses":["sourceAddresses","sourceAddresses"],"destinationPorts":["destinationPorts","destinationPorts"],"name":"name","description":"description","destinationAddresses":["destinationAddresses","destinationAddresses"],"protocols":["TCP","TCP"]},{"sourceAddresses":["sourceAddresses","sourceAddresses"],"destinationPorts":["destinationPorts","destinationPorts"],"name":"name","description":"description","destinationAddresses":["destinationAddresses","destinationAddresses"],"protocols":["TCP","TCP"]}],"priority":9613}}],"applicationRuleCollections":[{"name":"name","etag":"etag","properties":{"action":{"type":"Allow"},"rules":[{"sourceAddresses":["sourceAddresses","sourceAddresses"],"targetUrls":["targetUrls","targetUrls"],"name":"name","description":"description","protocols":[{"port":38575,"protocolType":"Http"},{"port":38575,"protocolType":"Http"}]},{"sourceAddresses":["sourceAddresses","sourceAddresses"],"targetUrls":["targetUrls","targetUrls"],"name":"name","description":"description","protocols":[{"port":38575,"protocolType":"Http"},{"port":38575,"protocolType":"Http"}]}],"provisioningState":"Succeeded","priority":5297}},{"name":"name","etag":"etag","properties":{"action":{"type":"Allow"},"rules":[{"sourceAddresses":["sourceAddresses","sourceAddresses"],"targetUrls":["targetUrls","targetUrls"],"name":"name","description":"description","protocols":[{"port":38575,"protocolType":"Http"},{"port":38575,"protocolType":"Http"}]},{"sourceAddresses":["sourceAddresses","sourceAddresses"],"targetUrls":["targetUrls","targetUrls"],"name":"name","description":"description","protocols":[{"port":38575,"protocolType":"Http"},{"port":38575,"protocolType":"Http"}]}],"provisioningState":"Succeeded","priority":5297}}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/azureFirewalls/{azure_firewall_name}'.format(resource_group_name='resource_group_name_example', azure_firewall_name='azure_firewall_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_firewalls_delete(client):
    """Test case for azure_firewalls_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/azureFirewalls/{azure_firewall_name}'.format(resource_group_name='resource_group_name_example', azure_firewall_name='azure_firewall_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_firewalls_get(client):
    """Test case for azure_firewalls_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/azureFirewalls/{azure_firewall_name}'.format(resource_group_name='resource_group_name_example', azure_firewall_name='azure_firewall_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_firewalls_list(client):
    """Test case for azure_firewalls_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/azureFirewalls'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_azure_firewalls_list_all(client):
    """Test case for azure_firewalls_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/azureFirewalls'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

