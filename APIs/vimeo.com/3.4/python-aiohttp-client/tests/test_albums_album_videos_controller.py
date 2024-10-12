# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album import Album
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.replace_videos_in_album_alt1_request import ReplaceVideosInAlbumAlt1Request
from openapi_server.models.set_video_as_album_thumbnail_alt1_request import SetVideoAsAlbumThumbnailAlt1Request
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_add_video_to_album(client):
    """Test case for add_video_to_album

    Add a specific video to an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/albums/{album_id}/videos/{video_id}'.format(album_id=12345, user_id=152184, video_id=196367152),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_to_album_alt1(client):
    """Test case for add_video_to_album_alt1

    Add a specific video to an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/albums/{album_id}/videos/{video_id}'.format(album_id=12345, video_id=196367152),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_video(client):
    """Test case for get_album_video

    Get a specific video in an album
    """
    params = [('password', 'hunter1')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}/videos/{video_id}'.format(album_id=3706071, user_id=152184, video_id=196367152),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_video_alt1(client):
    """Test case for get_album_video_alt1

    Get a specific video in an album
    """
    params = [('password', 'hunter1')]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/albums/{album_id}/videos/{video_id}'.format(album_id=3706071, video_id=196367152),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_videos(client):
    """Test case for get_album_videos

    Get all the videos in an album
    """
    params = [('containing_uri', '/videos/258684937'),
                    ('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('page', 1),
                    ('password', 'hunter1'),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example'),
                    ('weak_search', false)]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}/videos'.format(album_id=3706071, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_videos_alt1(client):
    """Test case for get_album_videos_alt1

    Get all the videos in an album
    """
    params = [('containing_uri', '/videos/258684937'),
                    ('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('filter_embeddable', true),
                    ('page', 1),
                    ('password', 'hunter1'),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example'),
                    ('weak_search', false)]
    headers = { 
        'Accept': 'application/vnd.vimeo.video+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/albums/{album_id}/videos'.format(album_id=3706071),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_video_from_album(client):
    """Test case for remove_video_from_album

    Remove a video from an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/albums/{album_id}/videos/{video_id}'.format(album_id=12345, user_id=152184, video_id=196367152),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_video_from_album_alt1(client):
    """Test case for remove_video_from_album_alt1

    Remove a video from an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/albums/{album_id}/videos/{video_id}'.format(album_id=12345, video_id=196367152),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_videos_in_album(client):
    """Test case for replace_videos_in_album

    Replace all the videos in an album
    """
    body = openapi_server.ReplaceVideosInAlbumAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/users/{user_id}/albums/{album_id}/videos'.format(album_id=3706071, user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_videos_in_album_alt1(client):
    """Test case for replace_videos_in_album_alt1

    Replace all the videos in an album
    """
    body = openapi_server.ReplaceVideosInAlbumAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/me/albums/{album_id}/videos'.format(album_id=3706071),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_video_as_album_thumbnail(client):
    """Test case for set_video_as_album_thumbnail

    Set a video as the album thumbnail
    """
    body = openapi_server.SetVideoAsAlbumThumbnailAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail'.format(album_id=12345, user_id=152184, video_id=196367152),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_video_as_album_thumbnail_alt1(client):
    """Test case for set_video_as_album_thumbnail_alt1

    Set a video as the album thumbnail
    """
    body = openapi_server.SetVideoAsAlbumThumbnailAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/me/albums/{album_id}/videos/{video_id}/set_album_thumbnail'.format(album_id=12345, video_id=196367152),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

