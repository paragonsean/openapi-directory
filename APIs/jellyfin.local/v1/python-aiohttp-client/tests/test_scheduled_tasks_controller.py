# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.task_info import TaskInfo
from openapi_server.models.task_trigger_info import TaskTriggerInfo


pytestmark = pytest.mark.asyncio

async def test_get_task(client):
    """Test case for get_task

    Get task by id.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ScheduledTasks/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tasks(client):
    """Test case for get_tasks

    Get tasks.
    """
    params = [('isHidden', True),
                    ('isEnabled', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ScheduledTasks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_task(client):
    """Test case for start_task

    Start specified task.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ScheduledTasks/Running/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_task(client):
    """Test case for stop_task

    Stop specified task.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ScheduledTasks/Running/{task_id}'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_task(client):
    """Test case for update_task

    Update specified task triggers.
    """
    body = {"DayOfWeek":"Sunday","Type":"Type","IntervalTicks":6,"TimeOfDayTicks":5,"MaxRuntimeTicks":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ScheduledTasks/{task_id}/Triggers'.format(task_id='task_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

