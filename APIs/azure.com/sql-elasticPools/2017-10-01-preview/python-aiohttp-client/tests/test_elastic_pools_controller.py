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
    parameters = {"kind":"kind","sku":"{}","properties":{"licenseType":"LicenseIncluded","perDatabaseSettings":{"maxCapacity":6.027456183070403,"minCapacity":1.4658129805029452},"maxSizeBytes":0,"zoneRedundant":True,"state":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_list_by_server(client):
    """Test case for elastic_pools_list_by_server

    
    """
    params = [('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elastic_pools_update(client):
    """Test case for elastic_pools_update

    
    """
    parameters = {"sku":{"size":"size","tier":"tier","name":"name","family":"family","capacity":6},"properties":{"licenseType":"LicenseIncluded","perDatabaseSettings":{"maxCapacity":6.027456183070403,"minCapacity":1.4658129805029452},"maxSizeBytes":0,"zoneRedundant":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/elasticPools/{elastic_pool_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', elastic_pool_name='elastic_pool_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

