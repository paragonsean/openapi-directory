# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.api_v2_cddrive_folders_folder_id_items_get200_response import ApiV2CddriveFoldersFolderIdItemsGet200Response
from openapi_server.models.cd_drive_file import CDDriveFile
from openapi_server.models.cd_drive_folder import CDDriveFolder


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_api_v2_cddrive_files_content_post(client):
    """Test case for api_v2_cddrive_files_content_post

    Upload a file.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_md5': 'content_md5_example',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('name', 'name_example')
    data.add_field('parent_id', 56)
    response = await client.request(
        method='POST',
        path='/api/v2/cddrive/files/content',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_files_file_id_content_get(client):
    """Test case for api_v2_cddrive_files_file_id_content_get

    UNDER DEVELOPMENT - Download a file.
    """
    headers = { 
        'Accept': 'application/octet-stream',
        'range': 'range_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/cddrive/files/{file_id}/content'.format(file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_files_file_id_delete(client):
    """Test case for api_v2_cddrive_files_file_id_delete

    Delete a file.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/cddrive/files/{file_id}'.format(file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_files_file_id_get(client):
    """Test case for api_v2_cddrive_files_file_id_get

    Get file information.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/cddrive/files/{file_id}'.format(file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_folders_folder_id_delete(client):
    """Test case for api_v2_cddrive_folders_folder_id_delete

    UNDER DEVELOPMENT - Delete a folder.
    """
    params = [('recursive', True)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/cddrive/folders/{folder_id}'.format(folder_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_folders_folder_id_get(client):
    """Test case for api_v2_cddrive_folders_folder_id_get

    UNDER DEVELOPMENT - Get folder information.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/cddrive/folders/{folder_id}'.format(folder_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v2_cddrive_folders_folder_id_items_get(client):
    """Test case for api_v2_cddrive_folders_folder_id_items_get

    Get the items in the folder.
    """
    params = [('offset', 0),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/cddrive/folders/{folder_id}/items'.format(folder_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_api_v2_cddrive_folders_post(client):
    """Test case for api_v2_cddrive_folders_post

    Create a folder.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'parent_id': 56
        }
    response = await client.request(
        method='POST',
        path='/api/v2/cddrive/folders',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

