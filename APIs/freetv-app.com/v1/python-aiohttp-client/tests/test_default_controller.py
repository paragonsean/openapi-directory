# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.latest_news_response import LatestNewsResponse


pytestmark = pytest.mark.asyncio

async def test_get_latest_news(client):
    """Test case for get_latest_news

    
    """
    params = [('language', 'language_example'),
                    ('category', 'category_example'),
                    ('keyword', 'keyword_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/services?funcs=GetLatestNewsForChatGPT&mobile=1',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

