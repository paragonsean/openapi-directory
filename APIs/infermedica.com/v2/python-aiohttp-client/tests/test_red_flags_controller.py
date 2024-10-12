# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.suggest_result import SuggestResult


pytestmark = pytest.mark.asyncio

async def test_compute_red_flags(client):
    """Test case for compute_red_flags

    Query the diagnostic engine for possible red flag symptoms
    """
    body = {"evidence":[{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"},{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"}],"sex":"male","extras":{"key":"{}"},"age":"18","evaluated_at":"2020-06-02"}
    params = [('max_results', 8)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/red_flags',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

