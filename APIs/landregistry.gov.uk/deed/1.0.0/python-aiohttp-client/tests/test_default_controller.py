# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deed_application import DeedApplication
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_deed(client):
    """Test case for add_deed

    Deed
    """
    body = openapi_server.DeedApplication()
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/deed/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

