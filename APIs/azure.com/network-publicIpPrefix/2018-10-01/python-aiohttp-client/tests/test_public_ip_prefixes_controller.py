# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.public_ip_prefix import PublicIPPrefix
from openapi_server.models.public_ip_prefix_list_result import PublicIPPrefixListResult
from openapi_server.models.public_ip_prefixes_update_tags_request import PublicIPPrefixesUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_create_or_update(client):
    """Test case for public_ip_prefixes_create_or_update

    
    """
    parameters = {"etag":"etag","sku":{"name":"Standard"},"zones":["zones","zones"],"properties":{"prefixLength":0,"publicIPAddressVersion":"IPv4","loadBalancerFrontendIpConfiguration":{"id":"id"},"resourceGuid":"resourceGuid","ipPrefix":"ipPrefix","publicIPAddresses":[{"id":"id"},{"id":"id"}],"provisioningState":"provisioningState","ipTags":[{"ipTagType":"ipTagType","tag":"tag"},{"ipTagType":"ipTagType","tag":"tag"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPPrefixes/{public_ip_prefix_name}'.format(resource_group_name='resource_group_name_example', public_ip_prefix_name='public_ip_prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_delete(client):
    """Test case for public_ip_prefixes_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPPrefixes/{public_ip_prefix_name}'.format(resource_group_name='resource_group_name_example', public_ip_prefix_name='public_ip_prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_get(client):
    """Test case for public_ip_prefixes_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPPrefixes/{public_ip_prefix_name}'.format(resource_group_name='resource_group_name_example', public_ip_prefix_name='public_ip_prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_list(client):
    """Test case for public_ip_prefixes_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPPrefixes'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_list_all(client):
    """Test case for public_ip_prefixes_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/publicIPPrefixes'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_public_ip_prefixes_update_tags(client):
    """Test case for public_ip_prefixes_update_tags

    
    """
    parameters = openapi_server.PublicIPPrefixesUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/publicIPPrefixes/{public_ip_prefix_name}'.format(resource_group_name='resource_group_name_example', public_ip_prefix_name='public_ip_prefix_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

