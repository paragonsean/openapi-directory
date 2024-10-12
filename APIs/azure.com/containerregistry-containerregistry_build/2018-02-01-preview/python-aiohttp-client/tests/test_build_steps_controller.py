# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_argument_list import BuildArgumentList
from openapi_server.models.build_step import BuildStep
from openapi_server.models.build_step_list import BuildStepList
from openapi_server.models.build_step_update_parameters import BuildStepUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_build_steps_create(client):
    """Test case for build_steps_create

    
    """
    build_step_create_parameters = {"properties":{"provisioningState":"Creating","type":"Docker"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps/{step_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example', step_name='step_name_example'),
        headers=headers,
        json=build_step_create_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_steps_delete(client):
    """Test case for build_steps_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps/{step_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example', step_name='step_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_steps_get(client):
    """Test case for build_steps_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps/{step_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example', step_name='step_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_steps_list(client):
    """Test case for build_steps_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_steps_list_build_arguments(client):
    """Test case for build_steps_list_build_arguments

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps/{step_name}/listBuildArguments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example', step_name='step_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_steps_update(client):
    """Test case for build_steps_update

    
    """
    build_step_update_parameters = {"properties":{"type":"Docker"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/buildTasks/{build_task_name}/steps/{step_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', build_task_name='build_task_name_example', step_name='step_name_example'),
        headers=headers,
        json=build_step_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

