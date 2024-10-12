# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.send_request import SendRequest


pytestmark = pytest.mark.asyncio

async def test_send(client):
    """Test case for send

    Send an email
    """
    body = {"subject":"subject","from":"from","html":"html","text":"text","to":"to"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/send',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

