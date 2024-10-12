# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.map import Map


pytestmark = pytest.mark.asyncio

async def test_trends_latest_get(client):
    """Test case for trends_latest_get

    List latest maps
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/trends/latest',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trends_recommended_get(client):
    """Test case for trends_recommended_get

    List recommended maps
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/trends/recommended',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

