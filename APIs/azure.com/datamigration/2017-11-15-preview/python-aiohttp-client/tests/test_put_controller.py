# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse
from openapi_server.models.projects_get200_response import ProjectsGet200Response
from openapi_server.models.services_get200_response import ServicesGet200Response
from openapi_server.models.tasks_get200_response import TasksGet200Response


pytestmark = pytest.mark.asyncio

async def test_projects_create_or_update_1(client):
    """Test case for projects_create_or_update_1

    Create or update project
    """
    parameters = openapi_server.ProjectsGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_create_or_update_1(client):
    """Test case for services_create_or_update_1

    Create or update DMS Instance
    """
    parameters = openapi_server.ServicesGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_create_or_update_1(client):
    """Test case for tasks_create_or_update_1

    Create or update task
    """
    parameters = openapi_server.TasksGet200Response()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example', task_name='task_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

