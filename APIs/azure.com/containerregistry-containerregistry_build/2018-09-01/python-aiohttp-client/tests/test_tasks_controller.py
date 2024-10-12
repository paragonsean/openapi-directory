# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.task import Task
from openapi_server.models.task_list_result import TaskListResult
from openapi_server.models.task_update_parameters import TaskUpdateParameters


pytestmark = pytest.mark.asyncio

async def test_tasks_create(client):
    """Test case for tasks_create

    
    """
    task_create_parameters = {"properties":{"agentConfiguration":{"cpu":0},"credentials":{"customRegistries":{"key":{"password":{"type":"Opaque","value":"value"},"userName":{"type":"Opaque","value":"value"}}},"sourceRegistry":{"loginMode":"None"}},"step":{"baseImageDependencies":[{"registry":"registry","digest":"digest","tag":"tag","repository":"repository","type":"BuildTime"},{"registry":"registry","digest":"digest","tag":"tag","repository":"repository","type":"BuildTime"}],"contextPath":"contextPath","type":"Docker","contextAccessToken":"contextAccessToken"},"provisioningState":"Creating","trigger":{"sourceTriggers":[{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"sourceControlType":"Github","branch":"branch","repositoryUrl":"repositoryUrl"},"sourceTriggerEvents":["commit","commit"],"name":"name","status":"Enabled"},{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"sourceControlType":"Github","branch":"branch","repositoryUrl":"repositoryUrl"},"sourceTriggerEvents":["commit","commit"],"name":"name","status":"Enabled"}],"baseImageTrigger":{"baseImageTriggerType":"All","name":"name","status":"Enabled"}},"creationDate":"2000-01-23T04:56:07.000+00:00","platform":{"os":"Windows","variant":"v6","architecture":"amd64"},"timeout":2582,"status":"Disabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_name='task_name_example'),
        headers=headers,
        json=task_create_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_delete(client):
    """Test case for tasks_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_get(client):
    """Test case for tasks_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_get_details(client):
    """Test case for tasks_get_details

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks/{task_name}/listDetails'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_list(client):
    """Test case for tasks_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_update(client):
    """Test case for tasks_update

    
    """
    task_update_parameters = {"properties":{"agentConfiguration":{"cpu":0},"credentials":{"customRegistries":{"key":{"password":{"type":"Opaque","value":"value"},"userName":{"type":"Opaque","value":"value"}}},"sourceRegistry":{"loginMode":"None"}},"step":{"contextPath":"contextPath","type":"Docker","contextAccessToken":"contextAccessToken"},"trigger":{"sourceTriggers":[{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"sourceControlType":"Github","branch":"branch","repositoryUrl":"repositoryUrl"},"sourceTriggerEvents":["commit","commit"],"name":"name","status":"Enabled"},{"sourceRepository":{"sourceControlAuthProperties":{"expiresIn":6,"scope":"scope","tokenType":"PAT","refreshToken":"refreshToken","token":"token"},"sourceControlType":"Github","branch":"branch","repositoryUrl":"repositoryUrl"},"sourceTriggerEvents":["commit","commit"],"name":"name","status":"Enabled"}],"baseImageTrigger":{"baseImageTriggerType":"All","name":"name","status":"Enabled"}},"platform":{"os":"Windows","variant":"v6","architecture":"amd64"},"timeout":0,"status":"Disabled"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example', task_name='task_name_example'),
        headers=headers,
        json=task_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

