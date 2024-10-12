# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.explanation_request import ExplanationRequest
from openapi_server.models.explanation_response import ExplanationResponse


pytestmark = pytest.mark.asyncio

async def test_compute_explanation(client):
    """Test case for compute_explanation

    Query diagnostic engine for explanation
    """
    body = {"evidence":[{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"},{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"}],"sex":"male","extras":{"key":"{}"},"age":"18","evaluated_at":"2020-06-02","target":"c_1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/explain',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

