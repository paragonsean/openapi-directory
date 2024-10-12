# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_workflow import CreateWorkflow
from openapi_server.models.error import Error
from openapi_server.models.response import Response


pytestmark = pytest.mark.asyncio

async def test_create_workflow(client):
    """Test case for create_workflow

    Create a workflow
    """
    body = openapi_server.CreateWorkflow()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/dispatch/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

