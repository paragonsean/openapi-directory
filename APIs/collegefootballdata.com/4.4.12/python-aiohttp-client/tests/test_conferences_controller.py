# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.conference import Conference


pytestmark = pytest.mark.asyncio

async def test_get_conferences(client):
    """Test case for get_conferences

    Conferences
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conferences',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

