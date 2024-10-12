# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.step import Step
from openapi_server.models.task import Task


pytestmark = pytest.mark.asyncio

async def test_v2_tasks_id_json_get(client):
    """Test case for v2_tasks_id_json_get

    Fetch a task
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/tasks/{id_jso}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_tasks_id_json_put(client):
    """Test case for v2_tasks_id_json_put

    Update a Task
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'current_state': 'current_state_example',
        'description': 'description_example',
        'due_date': 'due_date_example',
        'is_logged': True,
        'remind_at': 'remind_at_example',
        'subject': 'subject_example'
        }
    response = await client.request(
        method='PUT',
        path='/v2/tasks/{id_jso}'.format(id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_tasks_json_get(client):
    """Test case for v2_tasks_json_get

    List tasks
    """
    params = [('ids', [56]),
                    ('user_id', [56]),
                    ('person_id', [56]),
                    ('account_id', [56]),
                    ('current_state', ['current_state_example']),
                    ('task_type', ['task_type_example']),
                    ('time_interval_filter', 'time_interval_filter_example'),
                    ('idempotency_key', 'idempotency_key_example'),
                    ('locale', ['locale_example']),
                    ('sort_by', 'sort_by_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('per_page', 56),
                    ('page', 56),
                    ('include_paging_counts', True),
                    ('limit_paging_counts', True)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/tasks.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_v2_tasks_json_post(client):
    """Test case for v2_tasks_json_post

    Create a Task
    """
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'current_state': 'current_state_example',
        'description': 'description_example',
        'due_date': 'due_date_example',
        'idempotency_key': 'idempotency_key_example',
        'person_id': 'person_id_example',
        'remind_at': 'remind_at_example',
        'subject': 'subject_example',
        'task_type': 'task_type_example',
        'user_id': 56
        }
    response = await client.request(
        method='POST',
        path='/v2/tasks.json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

