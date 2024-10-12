# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.diagnosis_response_public import DiagnosisResponsePublic


pytestmark = pytest.mark.asyncio

async def test_compute_diagnosis(client):
    """Test case for compute_diagnosis

    Query diagnostic engine
    """
    body = {"evidence":[{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"},{"observed_at":"2020-06-02","id":"s_1","source":"initial","choice_id":"present"}],"sex":"male","extras":{"key":"{}"},"age":"18","evaluated_at":"2020-06-02"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/diagnosis',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

