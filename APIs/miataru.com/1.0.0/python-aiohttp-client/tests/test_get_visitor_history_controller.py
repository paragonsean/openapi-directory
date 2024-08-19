# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.miataru_get_visitor_history_request import MiataruGetVisitorHistoryRequest
from openapi_server.models.miataru_get_visitor_history_response import MiataruGetVisitorHistoryResponse


pytestmark = pytest.mark.asyncio

async def test_get_visitor_history(client):
    """Test case for get_visitor_history

    
    """
    body = {"MiataruGetVisitorHistory":{"Device":"7b8e6e0ee5296db345162dc2ef652c1350761823","Amount":"10"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/GetVisitorHistory',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

