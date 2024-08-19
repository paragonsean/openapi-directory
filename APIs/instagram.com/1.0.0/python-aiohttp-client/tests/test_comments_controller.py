# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comments_response import CommentsResponse
from openapi_server.models.status_response import StatusResponse


pytestmark = pytest.mark.asyncio

async def test_media_media_id_comments_comment_id_delete(client):
    """Test case for media_media_id_comments_comment_id_delete

    Remove a comment.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/media/{media_id}/comments/{comment_id}'.format(media_id='media_id_example', comment_id='comment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_media_id_comments_get(client):
    """Test case for media_media_id_comments_get

    Get a list of recent comments on a media object.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/{media_id}/comments'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_media_id_comments_post(client):
    """Test case for media_media_id_comments_post

    Create a comment on a media object.
    """
    params = [('text', 'text_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/media/{media_id}/comments'.format(media_id='media_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

