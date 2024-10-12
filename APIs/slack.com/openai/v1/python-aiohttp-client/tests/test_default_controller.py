# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ai_alpha_search_messages200_response import AiAlphaSearchMessages200Response
from openapi_server.models.search_request import SearchRequest


pytestmark = pytest.mark.asyncio

async def test_ai_alpha_search_messages(client):
    """Test case for ai_alpha_search_messages

    
    """
    body = openapi_server.SearchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/ai.alpha.search.messages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

