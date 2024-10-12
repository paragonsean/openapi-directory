# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.file_comment_entity import FileCommentEntity


pytestmark = pytest.mark.asyncio

async def test_delete_file_comments_id(client):
    """Test case for delete_file_comments_id

    Delete File Comment
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/file_comments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_comment_list_for_path(client):
    """Test case for file_comment_list_for_path

    List File Comments by path
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/file_comments/files/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_file_comments_id(client):
    """Test case for patch_file_comments_id

    Update File Comment
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/file_comments/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_file_comments(client):
    """Test case for post_file_comments

    Create File Comment
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('body', 'body_example')
    data.add_field('path', 'path_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/file_comments',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

