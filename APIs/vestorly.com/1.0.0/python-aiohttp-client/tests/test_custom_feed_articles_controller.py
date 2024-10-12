# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.articles import Articles


pytestmark = pytest.mark.asyncio

async def test_find_custom_feed_articles(client):
    """Test case for find_custom_feed_articles

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example'),
                    ('limit', 56),
                    ('sort_by', 'sort_by_example'),
                    ('start', 56),
                    ('created_at_gte_days_ago', 'created_at_gte_days_ago_example'),
                    ('text_query', 'text_query_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/custom_feeds/{id}/articles'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

