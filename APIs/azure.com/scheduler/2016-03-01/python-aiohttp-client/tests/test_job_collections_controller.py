# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job_collection_definition import JobCollectionDefinition
from openapi_server.models.job_collection_list_result import JobCollectionListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_job_collections_create_or_update(client):
    """Test case for job_collections_create_or_update

    
    """
    job_collection = {"name":"name","location":"location","id":"id","type":"type","properties":{"quota":{"maxJobCount":0,"maxRecurrence":{"interval":1,"frequency":"Minute"},"maxJobOccurrence":6},"state":"Enabled","sku":{"name":"Standard"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        json=job_collection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_delete(client):
    """Test case for job_collections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_disable(client):
    """Test case for job_collections_disable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/disable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_enable(client):
    """Test case for job_collections_enable

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}/enable'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_get(client):
    """Test case for job_collections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_list_by_resource_group(client):
    """Test case for job_collections_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_job_collections_list_by_subscription(client):
    """Test case for job_collections_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Scheduler/jobCollections'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_job_collections_patch(client):
    """Test case for job_collections_patch

    
    """
    job_collection = {"name":"name","location":"location","id":"id","type":"type","properties":{"quota":{"maxJobCount":0,"maxRecurrence":{"interval":1,"frequency":"Minute"},"maxJobOccurrence":6},"state":"Enabled","sku":{"name":"Standard"}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Scheduler/jobCollections/{job_collection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_collection_name='job_collection_name_example'),
        headers=headers,
        json=job_collection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

