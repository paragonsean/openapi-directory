# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_body1 import RequestBody1


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_session_schema_get(client):
    """Test case for v_custom_prices_session_schema_get

    Get custom prices schema
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_v/custom-prices/session/schema',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v_custom_prices_session_schema_post(client):
    """Test case for v_custom_prices_session_schema_post

    Create or Update custom prices schema
    """
    body = openapi_server.RequestBody1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/_v/custom-prices/session/schema',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

