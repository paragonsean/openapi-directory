# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article_phrases import ArticlePhrases


pytestmark = pytest.mark.asyncio

async def test_find_article_phrases(client):
    """Test case for find_article_phrases

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example'),
                    ('text_search', 'text_search_example'),
                    ('size', 56),
                    ('from', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/article_phrases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

