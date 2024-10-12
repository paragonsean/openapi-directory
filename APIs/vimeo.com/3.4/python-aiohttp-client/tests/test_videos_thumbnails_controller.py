# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_video_thumbnail_alt1_request import CreateVideoThumbnailAlt1Request
from openapi_server.models.edit_video_thumbnail_request import EditVideoThumbnailRequest
from openapi_server.models.picture import Picture


pytestmark = pytest.mark.asyncio

async def test_create_video_thumbnail(client):
    """Test case for create_video_thumbnail

    Add a video thumbnail
    """
    body = openapi_server.CreateVideoThumbnailAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/pictures'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_video_thumbnail_alt1(client):
    """Test case for create_video_thumbnail_alt1

    Add a video thumbnail
    """
    body = openapi_server.CreateVideoThumbnailAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/videos/{video_id}/pictures'.format(channel_id=927, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_thumbnail(client):
    """Test case for delete_video_thumbnail

    Delete a video thumbnail
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/pictures/{picture_id}'.format(picture_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_video_thumbnail(client):
    """Test case for edit_video_thumbnail

    Edit a video thumbnail
    """
    body = openapi_server.EditVideoThumbnailRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/pictures/{picture_id}'.format(picture_id=12345, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_thumbnail(client):
    """Test case for get_video_thumbnail

    Get a video thumbnail
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/pictures/{picture_id}'.format(picture_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_thumbnails(client):
    """Test case for get_video_thumbnails

    Get all the thumbnails of a video
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
        path='/videos/{video_id}/pictures'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_thumbnails_alt1(client):
    """Test case for get_video_thumbnails_alt1

    Get all the thumbnails of a video
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
        path='/channels/{channel_id}/videos/{video_id}/pictures'.format(channel_id=927, video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

