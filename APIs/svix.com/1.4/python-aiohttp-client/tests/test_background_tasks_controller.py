# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.background_task_out import BackgroundTaskOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_background_task_out import ListResponseBackgroundTaskOut
from openapi_server.models.ordering import Ordering


pytestmark = pytest.mark.asyncio

async def test_get_background_task_api_v1_background_task_task_id_get(client):
    """Test case for get_background_task_api_v1_background_task_task_id_get

    Get Background Task
    """
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/background-task/{task_id}'.format(task_id='qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_background_tasks_api_v1_background_task_get(client):
    """Test case for list_background_tasks_api_v1_background_task_get

    List Background Tasks
    """
    params = [('iterator', 'qtask_1srOrx2ZWZBpBUvZwXKQmoEYga2'),
                    ('limit', 50),
                    ('order', openapi_server.Ordering())]
    headers = { 
        'Accept': 'application/json',
        'idempotency_key': 'idempotency_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/background-task/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

