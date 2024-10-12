# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_list import FileList
from openapi_server.models.storage_update_file_request import StorageUpdateFileRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_storage_create_file(client):
    """Test case for storage_create_file

    Create File
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    data = FormData()
    data.add_field('file', 'file_example')
    data.add_field('read', ['read_example'])
    data.add_field('write', ['write_example'])
    response = await client.request(
        method='POST',
        path='/v1/storage/files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_delete_file(client):
    """Test case for storage_delete_file

    Delete File
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/storage/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_get_file(client):
    """Test case for storage_get_file

    Get File
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/storage/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_get_file_download(client):
    """Test case for storage_get_file_download

    Get File for Download
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/storage/files/{file_id}/download'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_get_file_preview(client):
    """Test case for storage_get_file_preview

    Get File Preview
    """
    params = [('width', 0),
                    ('height', 0),
                    ('gravity', 'center'),
                    ('quality', 100),
                    ('borderWidth', 0),
                    ('borderColor', ''),
                    ('borderRadius', 0),
                    ('opacity', 1),
                    ('rotation', 0),
                    ('background', ''),
                    ('output', '')]
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/storage/files/{file_id}/preview'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_get_file_view(client):
    """Test case for storage_get_file_view

    Get File for View
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/storage/files/{file_id}/view'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_list_files(client):
    """Test case for storage_list_files

    List Files
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/storage/files',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_storage_update_file(client):
    """Test case for storage_update_file

    Update File
    """
    body = openapi_server.StorageUpdateFileRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/storage/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

