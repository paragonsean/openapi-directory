# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_analytics_query_pack import LogAnalyticsQueryPack
from openapi_server.models.log_analytics_query_pack_list_result import LogAnalyticsQueryPackListResult
from openapi_server.models.tags_resource import TagsResource


pytestmark = pytest.mark.asyncio

async def test_query_packs_create_or_update(client):
    """Test case for query_packs_create_or_update

    
    """
    log_analytics_query_pack_payload = {"properties":{"queryPackId":"queryPackId","timeCreated":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","timeModified":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        json=log_analytics_query_pack_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_packs_delete(client):
    """Test case for query_packs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_packs_get(client):
    """Test case for query_packs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_packs_list(client):
    """Test case for query_packs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/microsoft.insights/queryPacks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_packs_list_by_resource_group(client):
    """Test case for query_packs_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_packs_update_tags(client):
    """Test case for query_packs_update_tags

    
    """
    query_pack_tags = {"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        json=query_pack_tags,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

