# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article_index import ArticleIndex


pytestmark = pytest.mark.asyncio

async def test_get_readinglist(client):
    """Test case for get_readinglist

    Readinglist
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/readinglist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

