# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.pipeline import Pipeline
from openapi_server.models.pipeline_list_result import PipelineListResult
from openapi_server.models.pipeline_update_parameters import PipelineUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_pipelines_create_or_update(client):
    """Test case for pipelines_create_or_update

    
    """
    create_operation_parameters = {"properties":{"bootstrapConfiguration":{"template":{"id":"id","parameters":{"key":"parameters"}},"repository":{"authorization":{"authorizationType":"personalAccessToken","parameters":{"key":"parameters"}},"defaultBranch":"defaultBranch","repositoryType":"gitHub","id":"id","properties":{"key":"properties"}}},"organization":{"name":"name","id":"id"},"project":{"name":"name","id":"id"},"pipelineId":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevOps/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        json=create_operation_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_delete(client):
    """Test case for pipelines_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevOps/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_get(client):
    """Test case for pipelines_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevOps/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_list_by_resource_group(client):
    """Test case for pipelines_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevOps/pipelines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_list_by_subscription(client):
    """Test case for pipelines_list_by_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DevOps/pipelines'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_update(client):
    """Test case for pipelines_update

    
    """
    update_operation_parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevOps/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        json=update_operation_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

