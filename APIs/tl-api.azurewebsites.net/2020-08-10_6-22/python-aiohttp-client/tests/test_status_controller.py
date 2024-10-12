# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.message_status import MessageStatus
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_status_get(client):
    """Test case for status_get

    Get the current status of message
    """
    params = [('messageId', 'message_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

