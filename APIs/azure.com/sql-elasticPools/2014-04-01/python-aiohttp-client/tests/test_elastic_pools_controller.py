# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.elastic_pool import ElasticPool
from openapi_server.models.elastic_pool_list_result import ElasticPoolListResult
from openapi_server.models.elastic_pool_update import ElasticPoolUpdate


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_create_or_update(client):
    """Test case for elastic_pools_create_or_update

    
    """
    parameters = {"kind":"kind","properties":{"databaseDtuMin":6,"databaseDtuMax":0,"dtu":1,"edition":"Basic","storageMB":5,"zoneRedundant":True,"state":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_delete(client):
    """Test case for elastic_pools_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_get(client):
    """Test case for elastic_pools_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_list_by_server(client):
    """Test case for elastic_pools_list_by_server

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_update(client):
    """Test case for elastic_pools_update

    
    """
    parameters = {"properties":{"databaseDtuMin":6,"databaseDtuMax":0,"dtu":1,"edition":"Basic","storageMB":5,"zoneRedundant":True,"state":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

