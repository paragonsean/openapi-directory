# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.comment_editable import CommentEditable


pytestmark = pytest.mark.asyncio

async def test_comments_id_delete(client):
    """Test case for comments_id_delete

    Delete comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/comments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_id_patch(client):
    """Test case for comments_id_patch

    Update comment
    """
    comment = {"body":"Nice photo"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/comments/{id}'.format(id=56),
        headers=headers,
        json=comment,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_comments_get(client):
    """Test case for maps_id_comments_get

    List comments for a given map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_comments_post(client):
    """Test case for maps_id_comments_post

    Create map comment
    """
    comment = {"body":"Nice photo"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/maps/{id}/comments'.format(id=56),
        headers=headers,
        json=comment,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_comments_get(client):
    """Test case for spots_id_comments_get

    List comments for a given spot
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/spots/{id}/comments'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spots_id_comments_post(client):
    """Test case for spots_id_comments_post

    Create spot comment
    """
    comment = {"body":"Nice photo"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/spots/{id}/comments'.format(id=56),
        headers=headers,
        json=comment,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

