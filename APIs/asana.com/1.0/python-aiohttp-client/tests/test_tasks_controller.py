# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_dependencies_for_task_request import AddDependenciesForTaskRequest
from openapi_server.models.add_dependents_for_task_request import AddDependentsForTaskRequest
from openapi_server.models.add_followers_request import AddFollowersRequest
from openapi_server.models.add_project_for_task_request import AddProjectForTaskRequest
from openapi_server.models.add_tag_for_task_request import AddTagForTaskRequest
from openapi_server.models.create_task201_response import CreateTask201Response
from openapi_server.models.create_task_request import CreateTaskRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.duplicate_task_request import DuplicateTaskRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_job200_response import GetJob200Response
from openapi_server.models.get_tasks_for_project200_response import GetTasksForProject200Response
from openapi_server.models.remove_follower_for_task_request import RemoveFollowerForTaskRequest
from openapi_server.models.remove_project_for_task_request import RemoveProjectForTaskRequest
from openapi_server.models.remove_tag_for_task_request import RemoveTagForTaskRequest
from openapi_server.models.set_parent_for_task_request import SetParentForTaskRequest


pytestmark = pytest.mark.asyncio

async def test_add_dependencies_for_task(client):
    """Test case for add_dependencies_for_task

    Set dependencies for a task
    """
    body = openapi_server.AddDependenciesForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/addDependencies'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_dependents_for_task(client):
    """Test case for add_dependents_for_task

    Set dependents for a task
    """
    body = openapi_server.AddDependentsForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/addDependents'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_followers_for_task(client):
    """Test case for add_followers_for_task

    Add followers to a task
    """
    body = {"followers":"521621,621373"}
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/addFollowers'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_project_for_task(client):
    """Test case for add_project_for_task

    Add a project to a task
    """
    body = openapi_server.AddProjectForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/addProject'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_tag_for_task(client):
    """Test case for add_tag_for_task

    Add a tag to a task
    """
    body = openapi_server.AddTagForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/addTag'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_subtask_for_task(client):
    """Test case for create_subtask_for_task

    Create a subtask
    """
    body = openapi_server.CreateTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/subtasks'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_task(client):
    """Test case for create_task

    Create a task
    """
    body = openapi_server.CreateTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_task(client):
    """Test case for delete_task

    Delete a task
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/1.0/tasks/{task_gid}'.format(task_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_duplicate_task(client):
    """Test case for duplicate_task

    Duplicate a task
    """
    body = openapi_server.DuplicateTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/duplicate'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dependencies_for_task(client):
    """Test case for get_dependencies_for_task

    Get dependencies from a task
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tasks/{task_gid}/dependencies'.format(task_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dependents_for_task(client):
    """Test case for get_dependents_for_task

    Get dependents from a task
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tasks/{task_gid}/dependents'.format(task_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_subtasks_for_task(client):
    """Test case for get_subtasks_for_task

    Get subtasks from a task
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tasks/{task_gid}/subtasks'.format(task_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_task(client):
    """Test case for get_task

    Get a task
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tasks/{task_gid}'.format(task_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks(client):
    """Test case for get_tasks

    Get multiple tasks
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'),
                    ('assignee', '14641'),
                    ('project', '321654'),
                    ('section', '321654'),
                    ('workspace', '321654'),
                    ('completed_since', '2012-02-22T02:06:58.158Z'),
                    ('modified_since', '2012-02-22T02:06:58.158Z')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_for_project(client):
    """Test case for get_tasks_for_project

    Get tasks from a project
    """
    params = [('completed_since', '2012-02-22T02:06:58.158Z'),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/projects/{project_gid}/tasks'.format(project_gid='1331'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_for_section(client):
    """Test case for get_tasks_for_section

    Get tasks from a section
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/sections/{section_gid}/tasks'.format(section_gid='321654'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_for_tag(client):
    """Test case for get_tasks_for_tag

    Get tasks from a tag
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/tags/{tag_gid}/tasks'.format(tag_gid='11235'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks_for_user_task_list(client):
    """Test case for get_tasks_for_user_task_list

    Get tasks from a user task list
    """
    params = [('completed_since', '2012-02-22T02:06:58.158Z'),
                    ('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('limit', 50),
                    ('offset', 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/user_task_lists/{user_task_list_gid}/tasks'.format(user_task_list_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_dependencies_for_task(client):
    """Test case for remove_dependencies_for_task

    Unlink dependencies from a task
    """
    body = openapi_server.AddDependenciesForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/removeDependencies'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_dependents_for_task(client):
    """Test case for remove_dependents_for_task

    Unlink dependents from a task
    """
    body = openapi_server.AddDependentsForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/removeDependents'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_follower_for_task(client):
    """Test case for remove_follower_for_task

    Remove followers from a task
    """
    body = openapi_server.RemoveFollowerForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/removeFollowers'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_project_for_task(client):
    """Test case for remove_project_for_task

    Remove a project from a task
    """
    body = openapi_server.RemoveProjectForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/removeProject'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tag_for_task(client):
    """Test case for remove_tag_for_task

    Remove a tag from a task
    """
    body = openapi_server.RemoveTagForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/removeTag'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_tasks_for_workspace(client):
    """Test case for search_tasks_for_workspace

    Search tasks in a workspace
    """
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]']),
                    ('text', 'Bug'),
                    ('resource_subtype', milestone),
                    ('assignee.any', '12345,23456,34567'),
                    ('assignee.not', '12345,23456,34567'),
                    ('portfolios.any', '12345,23456,34567'),
                    ('projects.any', '12345,23456,34567'),
                    ('projects.not', '12345,23456,34567'),
                    ('projects.all', '12345,23456,34567'),
                    ('sections.any', '12345,23456,34567'),
                    ('sections.not', '12345,23456,34567'),
                    ('sections.all', '12345,23456,34567'),
                    ('tags.any', '12345,23456,34567'),
                    ('tags.not', '12345,23456,34567'),
                    ('tags.all', '12345,23456,34567'),
                    ('teams.any', '12345,23456,34567'),
                    ('followers.not', '12345,23456,34567'),
                    ('created_by.any', '12345,23456,34567'),
                    ('created_by.not', '12345,23456,34567'),
                    ('assigned_by.any', '12345,23456,34567'),
                    ('assigned_by.not', '12345,23456,34567'),
                    ('liked_by.not', '12345,23456,34567'),
                    ('commented_on_by.not', '12345,23456,34567'),
                    ('due_on.before', '2019-09-15'),
                    ('due_on.after', '2019-09-15'),
                    ('due_on', '2019-09-15'),
                    ('due_at.before', '2019-04-15T01:01:46.055Z'),
                    ('due_at.after', '2019-04-15T01:01:46.055Z'),
                    ('start_on.before', '2019-09-15'),
                    ('start_on.after', '2019-09-15'),
                    ('start_on', '2019-09-15'),
                    ('created_on.before', '2019-09-15'),
                    ('created_on.after', '2019-09-15'),
                    ('created_on', '2019-09-15'),
                    ('created_at.before', '2019-04-15T01:01:46.055Z'),
                    ('created_at.after', '2019-04-15T01:01:46.055Z'),
                    ('completed_on.before', '2019-09-15'),
                    ('completed_on.after', '2019-09-15'),
                    ('completed_on', '2019-09-15'),
                    ('completed_at.before', '2019-04-15T01:01:46.055Z'),
                    ('completed_at.after', '2019-04-15T01:01:46.055Z'),
                    ('modified_on.before', '2019-09-15'),
                    ('modified_on.after', '2019-09-15'),
                    ('modified_on', '2019-09-15'),
                    ('modified_at.before', '2019-04-15T01:01:46.055Z'),
                    ('modified_at.after', '2019-04-15T01:01:46.055Z'),
                    ('is_blocking', false),
                    ('is_blocked', false),
                    ('has_attachment', false),
                    ('completed', false),
                    ('is_subtask', false),
                    ('sort_by', modified_at),
                    ('sort_ascending', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/1.0/workspaces/{workspace_gid}/tasks/search'.format(workspace_gid='12345'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_parent_for_task(client):
    """Test case for set_parent_for_task

    Set the parent of a task
    """
    body = openapi_server.SetParentForTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/1.0/tasks/{task_gid}/setParent'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_task(client):
    """Test case for update_task

    Update a task
    """
    body = openapi_server.CreateTaskRequest()
    params = [('opt_pretty', true),
                    ('opt_fields', ['[\"followers\",\"assignee\"]'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/1.0/tasks/{task_gid}'.format(task_gid='321654'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

