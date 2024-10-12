# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.task_status_list import TaskStatusList


pytestmark = pytest.mark.asyncio

async def test_task_status_get(client):
    """Test case for task_status_get

    Gets list of Task Statuses
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/TaskStatus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

