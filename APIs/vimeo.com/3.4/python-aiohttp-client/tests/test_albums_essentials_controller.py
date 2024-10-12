# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album import Album
from openapi_server.models.create_album_alt1_request import CreateAlbumAlt1Request
from openapi_server.models.edit_album_alt1_request import EditAlbumAlt1Request
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_create_album(client):
    """Test case for create_album

    Create an album
    """
    body = openapi_server.CreateAlbumAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Content-Type': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/albums'.format(user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_album_alt1(client):
    """Test case for create_album_alt1

    Create an album
    """
    body = openapi_server.CreateAlbumAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Content-Type': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/me/albums',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_album(client):
    """Test case for delete_album

    Delete an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/albums/{album_id}'.format(album_id=3706071, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_album_alt1(client):
    """Test case for delete_album_alt1

    Delete an album
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/me/albums/{album_id}'.format(album_id=3706071),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_album(client):
    """Test case for edit_album

    Edit an album
    """
    body = openapi_server.EditAlbumAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Content-Type': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}/albums/{album_id}'.format(album_id=3706071, user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_album_alt1(client):
    """Test case for edit_album_alt1

    Edit an album
    """
    body = openapi_server.EditAlbumAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Content-Type': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/me/albums/{album_id}'.format(album_id=3706071),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album(client):
    """Test case for get_album

    Get a specific album
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}'.format(album_id=3706071, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_alt1(client):
    """Test case for get_album_alt1

    Get a specific album
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.album+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/albums/{album_id}'.format(album_id=3706071),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_albums(client):
    """Test case for get_albums

    Get all the albums that belong to a user
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_albums_alt1(client):
    """Test case for get_albums_alt1

    Get all the albums that belong to a user
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/albums',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

