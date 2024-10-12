# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.task_type_list import TaskTypeList


pytestmark = pytest.mark.asyncio

async def test_task_type_get(client):
    """Test case for task_type_get

    Gets list of Task Types
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/TaskType',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

