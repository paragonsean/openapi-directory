# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.operations_list_default_response import OperationsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_projects_delete_1(client):
    """Test case for projects_delete_1

    Delete project
    """
    params = [('api-version', 'api_version_example'),
                    ('deleteRunningTasks', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_services_delete_1(client):
    """Test case for services_delete_1

    Delete DMS Service Instance
    """
    params = [('api-version', 'api_version_example'),
                    ('deleteRunningTasks', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tasks_delete_1(client):
    """Test case for tasks_delete_1

    Delete task
    """
    params = [('api-version', 'api_version_example'),
                    ('deleteRunningTasks', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{group_name}/providers/Microsoft.DataMigration/services/{service_name}/projects/{project_name}/tasks/{task_name}'.format(subscription_id='subscription_id_example', group_name='group_name_example', service_name='service_name_example', project_name='project_name_example', task_name='task_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

