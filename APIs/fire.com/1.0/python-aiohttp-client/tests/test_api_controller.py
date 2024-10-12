# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_application import ApiApplication
from openapi_server.models.new_api_application import NewApiApplication


pytestmark = pytest.mark.asyncio

async def test_create_api_application(client):
    """Test case for create_api_application

    Create a new API Application
    """
    body = openapi_server.NewApiApplication()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/apps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

