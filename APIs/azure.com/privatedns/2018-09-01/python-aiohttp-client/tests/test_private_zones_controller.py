# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_zone import PrivateZone
from openapi_server.models.private_zone_list_result import PrivateZoneListResult


pytestmark = pytest.mark.asyncio

async def test_private_zones_create_or_update(client):
    """Test case for private_zones_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"maxNumberOfVirtualNetworkLinksWithRegistration":1,"numberOfRecordSets":5,"numberOfVirtualNetworkLinksWithRegistration":2,"provisioningState":"Creating","maxNumberOfVirtualNetworkLinks":6,"numberOfVirtualNetworkLinks":5,"maxNumberOfRecordSets":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_zones_delete(client):
    """Test case for private_zones_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_zones_get(client):
    """Test case for private_zones_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_zones_list(client):
    """Test case for private_zones_list

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/privateDnsZones'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_zones_list_by_resource_group(client):
    """Test case for private_zones_list_by_resource_group

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_zones_update(client):
    """Test case for private_zones_update

    
    """
    parameters = {"etag":"etag","properties":{"maxNumberOfVirtualNetworkLinksWithRegistration":1,"numberOfRecordSets":5,"numberOfVirtualNetworkLinksWithRegistration":2,"provisioningState":"Creating","maxNumberOfVirtualNetworkLinks":6,"numberOfVirtualNetworkLinks":5,"maxNumberOfRecordSets":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

