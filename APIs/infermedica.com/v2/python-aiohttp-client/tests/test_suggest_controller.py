# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.suggest_request import SuggestRequest
from openapi_server.models.suggest_result import SuggestResult


pytestmark = pytest.mark.asyncio

async def test_get_suggestions(client):
    """Test case for get_suggestions

    Query diagnostic engine for related symptoms
    """
    body = {"evidence":[{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"},{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"}],"sex":"male","extras":{"key":"{}"},"age":"18","evaluated_at":"2020-06-02"}
    params = [('max_results', 8)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/suggest',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

