# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.test_dto import TestDTO


pytestmark = pytest.mark.asyncio

async def test_test_get(client):
    """Test case for test_get

    Get the all Test objects.             
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Test',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

