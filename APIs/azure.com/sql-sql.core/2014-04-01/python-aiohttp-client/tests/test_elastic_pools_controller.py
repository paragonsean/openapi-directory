# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.elastic_pool_activity_list_result import ElasticPoolActivityListResult
from openapi_server.models.elastic_pool_database_activity_list_result import ElasticPoolDatabaseActivityListResult


pytestmark = pytest.mark.asyncio

async def test_elastic_pool_activities_list_by_elastic_pool(client):
    """Test case for elastic_pool_activities_list_by_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}/elasticPoolActivity'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pool_database_activities_list_by_elastic_pool(client):
    """Test case for elastic_pool_database_activities_list_by_elastic_pool

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}/elasticPoolDatabaseActivity'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

