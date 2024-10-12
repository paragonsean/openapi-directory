# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment


pytestmark = pytest.mark.asyncio

async def test_get_comment_by_id(client):
    """Test case for get_comment_by_id

    Comment by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/comments/{id}'.format(id=321),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments_by_article_id(client):
    """Test case for get_comments_by_article_id

    Comments
    """
    params = [('a_id', '321'),
                    ('p_id', '321')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/comments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

