# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server.models.replace_album_logo_request import ReplaceAlbumLogoRequest


pytestmark = pytest.mark.asyncio

async def test_create_album_logo(client):
    """Test case for create_album_logo

    Add a custom album logo
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/albums/{album_id}/logos'.format(album_id=3706071, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_album_logo(client):
    """Test case for delete_album_logo

    Remove a custom album logo
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/users/{user_id}/albums/{album_id}/logos/{logo_id}'.format(album_id=3706071, logo_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_logo(client):
    """Test case for get_album_logo

    Get a specific custom album logo
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/albums/{album_id}/logos/{logo_id}'.format(album_id=3706071, logo_id=12345, user_id=152184),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_album_logos(client):
    """Test case for get_album_logos

    Get all the custom logos of an album
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
        path='/users/{user_id}/albums/{album_id}/logos'.format(album_id=3706071, user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_album_logo(client):
    """Test case for replace_album_logo

    Replace a custom album logo
    """
    body = openapi_server.ReplaceAlbumLogoRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.picture+json',
        'Content-Type': 'application/vnd.vimeo.picture+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/users/{user_id}/albums/{album_id}/logos/{logo_id}'.format(album_id=3706071, logo_id=12345, user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

