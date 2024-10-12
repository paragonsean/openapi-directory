# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_entity import FileEntity


pytestmark = pytest.mark.asyncio

async def test_folder_list_for_path(client):
    """Test case for folder_list_for_path

    List Folders by path
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('filter', 'filter_example'),
                    ('preview_size', 'preview_size_example'),
                    ('sort_by', None),
                    ('search', 'search_example'),
                    ('search_all', True),
                    ('with_previews', True),
                    ('with_priority_color', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/folders/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_folders_path(client):
    """Test case for post_folders_path

    Create folder
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('mkdir_parents', True)
    data.add_field('provided_mtime', '2013-10-20T19:20:30+01:00')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/folders/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

