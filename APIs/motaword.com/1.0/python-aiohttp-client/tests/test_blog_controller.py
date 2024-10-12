# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blog_article_list import BlogArticleList


pytestmark = pytest.mark.asyncio

async def test_get_blog_posts(client):
    """Test case for get_blog_posts

    Get blog posts - ordered by created desc by default
    """
    params = [('locale', 'locale_example'),
                    ('fallback', True),
                    ('page', 1),
                    ('per_page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/blogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

