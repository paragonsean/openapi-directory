# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.root200_response import Root200Response


pytestmark = pytest.mark.asyncio

async def test_root(client):
    """Test case for root

    Root
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/pcraig3/groundhog-day-api/1.2.1/api/v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spec(client):
    """Test case for spec

    Get JSON schema
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/pcraig3/groundhog-day-api/1.2.1/api/v1/spec',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

