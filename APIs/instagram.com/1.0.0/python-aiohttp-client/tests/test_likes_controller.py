# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.status_response import StatusResponse
from openapi_server.models.users_info_response import UsersInfoResponse


pytestmark = pytest.mark.asyncio

async def test_media_media_id_likes_delete(client):
    """Test case for media_media_id_likes_delete

    Remove a like on this media by the current user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/media/{media_id}/likes'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_media_id_likes_get(client):
    """Test case for media_media_id_likes_get

    Get a list of users who have liked this media.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/media/{media_id}/likes'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_media_id_likes_post(client):
    """Test case for media_media_id_likes_post

    Set a like on this media by the current user.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/media/{media_id}/likes'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

