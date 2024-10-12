# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.create_comment_alt1_request import CreateCommentAlt1Request
from openapi_server.models.create_comment_reply_request import CreateCommentReplyRequest
from openapi_server.models.edit_comment_request import EditCommentRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_create_comment(client):
    """Test case for create_comment

    Add a comment to a video
    """
    body = openapi_server.CreateCommentAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Content-Type': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/comments'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_comment_alt1(client):
    """Test case for create_comment_alt1

    Add a comment to a video
    """
    body = openapi_server.CreateCommentAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Content-Type': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/videos/{video_id}/comments'.format(channel_id=927, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_comment_reply(client):
    """Test case for create_comment_reply

    Add a reply to a video comment
    """
    body = openapi_server.CreateCommentReplyRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Content-Type': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/comments/{comment_id}/replies'.format(comment_id=12345, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_comment(client):
    """Test case for delete_comment

    Delete a video comment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/comments/{comment_id}'.format(comment_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_comment(client):
    """Test case for edit_comment

    Edit a video comment
    """
    body = openapi_server.EditCommentRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Content-Type': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/comments/{comment_id}'.format(comment_id=12345, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comment(client):
    """Test case for get_comment

    Get a specific video comment
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/comments/{comment_id}'.format(comment_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comment_replies(client):
    """Test case for get_comment_replies

    Get all the replies to a video comment
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/comments/{comment_id}/replies'.format(comment_id=12345, video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments(client):
    """Test case for get_comments

    Get all the comments on a video
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/comments'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments_alt1(client):
    """Test case for get_comments_alt1

    Get all the comments on a video
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.comment+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/videos/{video_id}/comments'.format(channel_id=927, video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

