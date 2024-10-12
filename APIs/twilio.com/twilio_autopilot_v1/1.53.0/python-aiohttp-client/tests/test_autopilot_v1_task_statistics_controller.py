# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_task_statistics import AutopilotV1AssistantTaskTaskStatistics


pytestmark = pytest.mark.asyncio

async def test_fetch_task_statistics(client):
    """Test case for fetch_task_statistics

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Statistics'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

