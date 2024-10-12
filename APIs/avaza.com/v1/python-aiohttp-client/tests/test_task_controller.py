# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.new_task import NewTask
from openapi_server.models.task_details import TaskDetails
from openapi_server.models.task_dropdown_list import TaskDropdownList
from openapi_server.models.task_list import TaskList
from openapi_server.models.update_task import UpdateTask


pytestmark = pytest.mark.asyncio

async def test_task_delete(client):
    """Test case for task_delete

    Delete a Task
    """
    params = [('TaskID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_get(client):
    """Test case for task_get

    Gets list of Tasks
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example'),
                    ('isComplete', True),
                    ('ProjectID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Task',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_get_by_id(client):
    """Test case for task_get_by_id

    Gets Task by Task ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Task/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_task_lookup(client):
    """Test case for task_lookup

    Gets minimal list of Tasks for the current user
    """
    params = [('projectID', 56),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('hideCompleted', True),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Task/Lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_task_post(client):
    """Test case for task_post

    Create a Task
    """
    model = {"EstimatedEffort":1.4658129805029452,"AssignedToUserIDFKs":[6,6],"SectionIDFK":5,"AccountTaskTypeIDFK":0,"Description":"Description","DateStart":"2000-01-23T04:56:07.000+00:00","ProjectIDFK":5,"DateDue":"2000-01-23T04:56:07.000+00:00","Title":"Title","TaskPriorityCode":"TaskPriorityCode","Tags":[{"Color":"Color","Name":"Name"},{"Color":"Color","Name":"Name"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Task',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_task_put(client):
    """Test case for task_put

    Update a Task.
    """
    model = {"EstimatedEffort":6.027456183070403,"SectionIDFK":5,"Description":"Description","FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"TaskID":5,"TaskStatusCode":"TaskStatusCode","DateStart":"2000-01-23T04:56:07.000+00:00","Title":"Title","TaskPriorityCode":"TaskPriorityCode","PercentComplete":1,"DateDue":"2000-01-23T04:56:07.000+00:00","Tags":[{"Color":"Color","Name":"Name"},{"Color":"Color","Name":"Name"}],"AssignedToUserIDFK":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Task',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

