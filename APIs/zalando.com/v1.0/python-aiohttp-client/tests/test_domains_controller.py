# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain


pytestmark = pytest.mark.asyncio

async def test_domains_get(client):
    """Test case for domains_get

    Shop Domains
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

