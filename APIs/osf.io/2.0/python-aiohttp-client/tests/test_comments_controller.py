# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment


pytestmark = pytest.mark.asyncio

async def test_comments_delete(client):
    """Test case for comments_delete

    Delete a comment
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/comments/{comment_id}'.format(comment_id='comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_put(client):
    """Test case for comments_put

    Update a comment
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/comments/{comment_id}'.format(comment_id='comment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_read(client):
    """Test case for comments_read

    Retrieve a comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/comments/{comment_id}'.format(comment_id='comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

