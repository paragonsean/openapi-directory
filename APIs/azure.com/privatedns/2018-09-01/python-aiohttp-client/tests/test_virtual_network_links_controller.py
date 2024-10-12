# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.virtual_network_link import VirtualNetworkLink
from openapi_server.models.virtual_network_link_list_result import VirtualNetworkLinkListResult


pytestmark = pytest.mark.asyncio

async def test_virtual_network_links_create_or_update(client):
    """Test case for virtual_network_links_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"registrationEnabled":True,"provisioningState":"Creating","virtualNetworkLinkState":"InProgress","virtualNetwork":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/virtualNetworkLinks/{virtual_network_link_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', virtual_network_link_name='virtual_network_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_links_delete(client):
    """Test case for virtual_network_links_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/virtualNetworkLinks/{virtual_network_link_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', virtual_network_link_name='virtual_network_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_links_get(client):
    """Test case for virtual_network_links_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/virtualNetworkLinks/{virtual_network_link_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', virtual_network_link_name='virtual_network_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_links_list(client):
    """Test case for virtual_network_links_list

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/virtualNetworkLinks'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_links_update(client):
    """Test case for virtual_network_links_update

    
    """
    parameters = {"etag":"etag","properties":{"registrationEnabled":True,"provisioningState":"Creating","virtualNetworkLinkState":"InProgress","virtualNetwork":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/virtualNetworkLinks/{virtual_network_link_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', virtual_network_link_name='virtual_network_link_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

