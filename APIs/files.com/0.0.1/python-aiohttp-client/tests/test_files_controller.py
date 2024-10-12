# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.file_entity import FileEntity


pytestmark = pytest.mark.asyncio

async def test_delete_files_path(client):
    """Test case for delete_files_path

    Delete file/folder
    """
    params = [('recursive', True)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/files/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_download(client):
    """Test case for file_download

    Download file
    """
    params = [('action', 'action_example'),
                    ('preview_size', 'preview_size_example'),
                    ('with_previews', True),
                    ('with_priority_color', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/files/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_files_path(client):
    """Test case for patch_files_path

    Update file/folder metadata
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('priority_color', 'priority_color_example')
    data.add_field('provided_mtime', '2013-10-20T19:20:30+01:00')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/files/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_files_path(client):
    """Test case for post_files_path

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('action', 'action_example')
    data.add_field('etags_etag', ['etags_etag_example'])
    data.add_field('etags_part', [56])
    data.add_field('length', 56)
    data.add_field('mkdir_parents', True)
    data.add_field('part', 56)
    data.add_field('parts', 56)
    data.add_field('provided_mtime', '2013-10-20T19:20:30+01:00')
    data.add_field('ref', 'ref_example')
    data.add_field('restart', 56)
    data.add_field('size', 56)
    data.add_field('structure', 'structure_example')
    data.add_field('with_rename', True)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/files/{path}'.format(path='path_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

