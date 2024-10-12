# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.venue import Venue


pytestmark = pytest.mark.asyncio

async def test_get_venues(client):
    """Test case for get_venues

    Arena and venue information
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/venues',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

