# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_a_comment_request import PostACommentRequest
from openapi_server.models.post_a_reply_for_a_comment_request import PostAReplyForACommentRequest
from openapi_server.models.update_a_comment_or_reply_request import UpdateACommentOrReplyRequest


pytestmark = pytest.mark.asyncio

async def test_delete_a_comment_or_reply(client):
    """Test case for delete_a_comment_or_reply

    Delete a comment or reply
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/comments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_comment_or_reply(client):
    """Test case for get_a_comment_or_reply

    Get a comment or reply
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/{id}'.format(id='417'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_users_who_liked_a_comment(client):
    """Test case for get_all_users_who_liked_a_comment

    Get all users who liked a comment
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/{id}/likes'.format(id=417),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recently_created_comments(client):
    """Test case for get_recently_created_comments

    Get recently created comments
    """
    params = [('include_replies', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/recent/{comment_type}/{type}'.format(comment_type='all', type='all'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recently_updated_comments(client):
    """Test case for get_recently_updated_comments

    Get recently updated comments
    """
    params = [('include_replies', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/updates/{comment_type}/{type}'.format(comment_type='all', type='all'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_replies_for_a_comment(client):
    """Test case for get_replies_for_a_comment

    Get replies for a comment
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/{id}/replies'.format(id='417'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_the_attached_media_item(client):
    """Test case for get_the_attached_media_item

    Get the attached media item
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/{id}/item'.format(id=417),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trending_comments(client):
    """Test case for get_trending_comments

    Get trending comments
    """
    params = [('include_replies', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/comments/trending/{comment_type}/{type}'.format(comment_type='all', type='all'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_like_a_comment(client):
    """Test case for like_a_comment

    Like a comment
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/comments/{id}/like'.format(id='417'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_a_comment(client):
    """Test case for post_a_comment

    Post a comment
    """
    body = openapi_server.PostACommentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/comments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_a_reply_for_a_comment(client):
    """Test case for post_a_reply_for_a_comment

    Post a reply for a comment
    """
    body = openapi_server.PostAReplyForACommentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/comments/{id}/replies'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_like_on_a_comment(client):
    """Test case for remove_like_on_a_comment

    Remove like on a comment
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/comments/{id}/like'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_a_comment_or_reply(client):
    """Test case for update_a_comment_or_reply

    Update a comment or reply
    """
    body = openapi_server.UpdateACommentOrReplyRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/comments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

