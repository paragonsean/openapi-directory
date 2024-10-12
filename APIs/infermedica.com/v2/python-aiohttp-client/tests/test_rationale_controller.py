# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rationale_request import RationaleRequest
from openapi_server.models.rationale_response import RationaleResponse


pytestmark = pytest.mark.asyncio

async def test_compute_rationale(client):
    """Test case for compute_rationale

    Query diagnostic engine for question rationale
    """
    body = {"evidence":[{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"},{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"}],"sex":"male","extras":{"key":"{}"},"age":"18","evaluated_at":"2020-06-02"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/rationale',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

