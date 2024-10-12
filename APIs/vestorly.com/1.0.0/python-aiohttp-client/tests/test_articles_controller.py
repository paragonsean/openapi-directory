# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.articleresponse import Articleresponse
from openapi_server.models.articles import Articles


pytestmark = pytest.mark.asyncio

async def test_find_article_by_id(client):
    """Test case for find_article_by_id

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/articles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_articles(client):
    """Test case for find_articles

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example'),
                    ('limit', 56),
                    ('text_query', 'text_query_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('sort_by', 'sort_by_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

