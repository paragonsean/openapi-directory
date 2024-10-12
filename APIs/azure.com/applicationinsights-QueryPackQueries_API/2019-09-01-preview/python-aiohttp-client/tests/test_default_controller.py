# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_analytics_query_pack_query import LogAnalyticsQueryPackQuery
from openapi_server.models.log_analytics_query_pack_query_list_result import LogAnalyticsQueryPackQueryListResult
from openapi_server.models.log_analytics_query_pack_query_search_properties import LogAnalyticsQueryPackQuerySearchProperties


pytestmark = pytest.mark.asyncio

async def test_queries_delete(client):
    """Test case for queries_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}/queries/{query_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', query_pack_name='query_pack_name_example', query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queries_get(client):
    """Test case for queries_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}/queries/{query_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', query_pack_name='query_pack_name_example', query_id='query_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queries_list(client):
    """Test case for queries_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('includeBody', True),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}/queries'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queries_put(client):
    """Test case for queries_put

    
    """
    query_payload = {"properties":{"resourceTypes":["resourceTypes","resourceTypes"],"linkedResourceId":"linkedResourceId","author":"author","displayName":"displayName","description":"description","timeCreated":"2000-01-23T04:56:07.000+00:00","categories":["categories","categories"],"body":"body","timeModified":"2000-01-23T04:56:07.000+00:00","labels":["labels","labels"],"queryId":"queryId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}/queries/{query_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', query_pack_name='query_pack_name_example', query_id='query_id_example'),
        headers=headers,
        json=query_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_queries_search(client):
    """Test case for queries_search

    
    """
    query_search_properties = {"resourceTypes":["resourceTypes","resourceTypes"],"categories":["categories","categories"],"labels":["labels","labels"]}
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('includeBody', True),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/microsoft.insights/queryPacks/{query_pack_name}/queries/search'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', query_pack_name='query_pack_name_example'),
        headers=headers,
        json=query_search_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

