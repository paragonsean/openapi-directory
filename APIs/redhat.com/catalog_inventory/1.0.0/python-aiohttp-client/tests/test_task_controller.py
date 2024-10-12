# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.task import Task
from openapi_server.models.tasks_collection import TasksCollection


pytestmark = pytest.mark.asyncio

async def test_list_tasks(client):
    """Test case for list_tasks

    List Tasks
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', None),
                    ('sort_by', None)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/tasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_show_task(client):
    """Test case for show_task

    Show an existing Task
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='//api/catalog-inventory/v1.0/tasks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_task(client):
    """Test case for update_task

    Update an existing Task
    """
    body = {"owner":"jdoe","archived_at":"2000-01-23T04:56:07.000+00:00","target_type":"target_type","created_at":"2000-01-23T04:56:07.000+00:00","message":"received message starting inventory collection","type":"CloudConnectorTask","output":"Result of Task Execution","completed_at":"2000-01-23T04:56:07.000+00:00","input":"Task payload input content","updated_at":"2000-01-23T04:56:07.000+00:00","child_task_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","controller_message_id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"Order Service Plan","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","source_id":"source_id","state":"running","target_source_ref":"target_source_ref","status":"error"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='//api/catalog-inventory/v1.0/tasks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

