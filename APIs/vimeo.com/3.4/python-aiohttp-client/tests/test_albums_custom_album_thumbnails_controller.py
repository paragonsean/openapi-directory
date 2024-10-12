# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server.models.replace_album_custom_thumb_request import ReplaceAlbumCustomThumbRequest


pytestmark = pytest.mark.asyncio

async def test_create_album_custom_thumb(client):
    """Test case for create_album_custom_thumb

    Add a custom uploaded thumbnail
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/albums/{album_id}/custom_thumbnails'.format(album_id=3706071, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_album_custom_thumbnail(client):
    """Test case for delete_album_custom_thumbnail

    Remove a custom uploaded album thumbnail
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}'.format(album_id=3706071, thumbnail_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_custom_thumbnail(client):
    """Test case for get_album_custom_thumbnail

    Get a specific custom uploaded album thumbnail
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}'.format(album_id=3706071, thumbnail_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_custom_thumbs(client):
    """Test case for get_album_custom_thumbs

    Get all the custom upload thumbnails of an album
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}/custom_thumbnails'.format(album_id=3706071, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_album_custom_thumb(client):
    """Test case for replace_album_custom_thumb

    Replace a custom uploaded album thumbnail
    """
    body = openapi_server.ReplaceAlbumCustomThumbRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}'.format(album_id=3706071, thumbnail_id=12345, user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

