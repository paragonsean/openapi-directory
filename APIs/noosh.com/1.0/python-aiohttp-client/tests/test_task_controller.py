# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.task_created_vo import TaskCreatedVO
from openapi_server.models.task_expand_vo import TaskExpandVO
from openapi_server.models.task_expand_workgroup_level_vo import TaskExpandWorkgroupLevelVO
from openapi_server.models.task_list_vo import TaskListVO
from openapi_server.models.task_persist_vo import TaskPersistVO
from openapi_server.models.task_priority_list_vo import TaskPriorityListVO
from openapi_server.models.task_status_list_vo import TaskStatusListVO
from openapi_server.models.task_type_list_vo import TaskTypeListVO
from openapi_server.models.task_workgroup_level_list_vo import TaskWorkgroupLevelListVO
from openapi_server.models.wg_task_status_list_vo import WgTaskStatusListVO


pytestmark = pytest.mark.asyncio

async def test_get_custom_task_types_of_wg(client):
    """Test case for get_custom_task_types_of_wg

    Get custom task types of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/customTaskTypes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_task_status_list(client):
    """Test case for get_default_task_status_list

    Get default task status list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/defaultTaskStatus'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_list_of_project(client):
    """Test case for get_task_list_of_project

    Get task list of project level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/tasks'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_list_of_workgroup(client):
    """Test case for get_task_list_of_workgroup

    Get task list of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/tasks'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_of_project(client):
    """Test case for get_task_of_project

    Get a sepcific task of project level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/tasks/{task_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_of_workgroup(client):
    """Test case for get_task_of_workgroup

    Get a sepcific task of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/tasks/{task_id}'.format(workgroup_id='workgroup_id_example', task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task_types_of_workgroup(client):
    """Test case for get_task_types_of_workgroup

    Get task types of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/taskTypes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wg_task_status_list_of_workgroup(client):
    """Test case for get_wg_task_status_list_of_workgroup

    Get custom task status of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/customTaskStatus'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_task_for_project(client):
    """Test case for post_task_for_project

    Create a new task
    """
    body = {"actual_duration":1.1,"comments":"sample comments","percentage_complete":1,"actual_start_date":"2000-01-23","revised_end_date":"2000-01-23","custom_status_id":1,"description":"sample description","task_id":1,"priority":1,"actual_duration_hour":1.1,"revised_duration_hour":1.1,"assign_to_user_id":1,"actual_end_date":"2000-01-23","status_id":1,"task_type_id":1,"name":"sample name","revised_duration":1.1,"contributors":"sample contributors","revised_start_date":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/tasks'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_priority_list(client):
    """Test case for task_priority_list

    Get default task priority list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/defaultTaskPriority'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

