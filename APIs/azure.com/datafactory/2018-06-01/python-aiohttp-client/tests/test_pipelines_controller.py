# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_run_response import CreateRunResponse
from openapi_server.models.pipeline_list_response import PipelineListResponse
from openapi_server.models.pipeline_resource import PipelineResource


pytestmark = pytest.mark.asyncio

async def test_pipelines_create_or_update(client):
    """Test case for pipelines_create_or_update

    
    """
    pipeline = {"properties":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        json=pipeline,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_create_run(client):
    """Test case for pipelines_create_run

    
    """
    parameters = None
    params = [('api-version', 'api_version_example'),
                    ('referencePipelineRunId', 'reference_pipeline_run_id_example'),
                    ('isRecovery', True),
                    ('startActivityName', 'start_activity_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelines/{pipeline_name}/createRun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        json=parameters,
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', pipeline_name='pipeline_name_example'),
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
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelines/{pipeline_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example', pipeline_name='pipeline_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pipelines_list_by_factory(client):
    """Test case for pipelines_list_by_factory

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/pipelines'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

