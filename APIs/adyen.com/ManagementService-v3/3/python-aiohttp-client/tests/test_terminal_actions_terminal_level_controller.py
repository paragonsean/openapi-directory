# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.schedule_terminal_actions_request import ScheduleTerminalActionsRequest
from openapi_server.models.schedule_terminal_actions_response import ScheduleTerminalActionsResponse


pytestmark = pytest.mark.asyncio

async def test_post_terminals_schedule_actions(client):
    """Test case for post_terminals_schedule_actions

    Create a terminal action
    """
    body = {"actionDetails":{"appId":"appId","type":"InstallAndroidApp"},"storeId":"storeId","terminalIds":["terminalIds","terminalIds"],"scheduledAt":"scheduledAt"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/terminals/scheduleActions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

