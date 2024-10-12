# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.recommended_elastic_pool import RecommendedElasticPool
from openapi_server.models.recommended_elastic_pool_list_metrics_result import RecommendedElasticPoolListMetricsResult
from openapi_server.models.recommended_elastic_pool_list_result import RecommendedElasticPoolListResult


pytestmark = pytest.mark.asyncio

async def test_recommended_elastic_pools_get(client):
    """Test case for recommended_elastic_pools_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/recommendedElasticPools/{recommended_elastic_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', recommended_elastic_pool_name='recommended_elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommended_elastic_pools_list_by_server(client):
    """Test case for recommended_elastic_pools_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/recommendedElasticPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recommended_elastic_pools_list_metrics(client):
    """Test case for recommended_elastic_pools_list_metrics

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/recommendedElasticPools/{recommended_elastic_pool_name}/metrics'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', recommended_elastic_pool_name='recommended_elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

