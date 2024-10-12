# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.news_get200_response import NewsGet200Response


pytestmark = pytest.mark.asyncio

async def test_news_get(client):
    """Test case for news_get

    Get Fortnite News
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/news',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

