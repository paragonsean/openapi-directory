# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_task import BuildTask
from openapi_server.models.build_task_list_result import BuildTaskListResult
from openapi_server.models.build_task_update_parameters import BuildTaskUpdateParameters
from openapi_server.models.source_repository_properties import SourceRepositoryProperties


pytestmark = pytest.mark.asyncio

async def test_build_tasks_create(client):
    """Test case for build_tasks_create

    
    """
    build_task_create_parameters = {"properties":{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"sourceControlType":"Github","isCommitTriggerEnabled":False,"repositoryUrl":"repositoryUrl"},"alias":"alias","provisioningState":"Creating","creationDate":"2000-01-23T04:56:07.000+00:00","platform":{"osType":"Windows","cpu":0},"timeout":4477,"status":"Disabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        json=build_task_create_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_tasks_delete(client):
    """Test case for build_tasks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_tasks_get(client):
    """Test case for build_tasks_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_tasks_list(client):
    """Test case for build_tasks_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_tasks_list_source_repository_properties(client):
    """Test case for build_tasks_list_source_repository_properties

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/listSourceRepositoryProperties'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_tasks_update(client):
    """Test case for build_tasks_update

    
    """
    build_task_update_parameters = {"properties":{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"isCommitTriggerEnabled":True},"alias":"alias","platform":{"osType":"Windows","cpu":0},"timeout":2582,"status":"Disabled"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        json=build_task_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

