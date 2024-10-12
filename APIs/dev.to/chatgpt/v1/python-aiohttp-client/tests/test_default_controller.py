# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_articles_response import GetArticlesResponse


pytestmark = pytest.mark.asyncio

async def test_get_articles(client):
    """Test case for get_articles

    Get a list of filtered articles
    """
    params = [('q', 'q_example'),
                    ('page', 0),
                    ('per_page', 60),
                    ('top', 'top_example')]
    headers = { 
        'Accept': 'application/vnd.forem.api-v1+json',
    }
    response = await client.request(
        method='GET',
        path='/api/articles/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

