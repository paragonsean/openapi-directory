# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_folder import CollectionResponseFolder
from openapi_server.models.error import Error
from openapi_server.models.folder import Folder
from openapi_server.models.folder_action_response import FolderActionResponse
from openapi_server.models.folder_input import FolderInput
from openapi_server.models.folder_update_input import FolderUpdateInput
from openapi_server.models.folder_update_task_locator import FolderUpdateTaskLocator


pytestmark = pytest.mark.asyncio

async def test_delete_files_v3_folders_folder_id_archive(client):
    """Test case for delete_files_v3_folders_folder_id_archive

    Delete folder.
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files/v3/folders/{folder_id}'.format(folder_id='folder_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_files_v3_folders_folder_path_archive_by_path(client):
    """Test case for delete_files_v3_folders_folder_path_archive_by_path

    Delete folder.
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files/v3/folders/{folder_path}'.format(folder_path='folder_path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_folders_folder_id_get_by_id(client):
    """Test case for get_files_v3_folders_folder_id_get_by_id

    Get folder
    """
    params = [('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/folders/{folder_id}'.format(folder_id='folder_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_folders_folder_path_get_by_path(client):
    """Test case for get_files_v3_folders_folder_path_get_by_path

    Get folder.
    """
    params = [('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/folders/{folder_path}'.format(folder_path='folder_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_folders_search_do_search(client):
    """Test case for get_files_v3_folders_search_do_search

    Search folders
    """
    params = [('properties', ['properties_example']),
                    ('after', 'after_example'),
                    ('before', 'before_example'),
                    ('limit', 56),
                    ('sort', ['sort_example']),
                    ('id', 'id_example'),
                    ('createdAt', '2013-10-20T19:20:30+01:00'),
                    ('createdAtLte', '2013-10-20T19:20:30+01:00'),
                    ('createdAtGte', '2013-10-20T19:20:30+01:00'),
                    ('updatedAt', '2013-10-20T19:20:30+01:00'),
                    ('updatedAtLte', '2013-10-20T19:20:30+01:00'),
                    ('updatedAtGte', '2013-10-20T19:20:30+01:00'),
                    ('name', 'name_example'),
                    ('path', 'path_example'),
                    ('parentFolderId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/folders/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_folders_update_async_tasks_task_id_status_check_update_status(client):
    """Test case for get_files_v3_folders_update_async_tasks_task_id_status_check_update_status

    Check folder update status.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/folders/update/async/tasks/{task_id}/status'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_files_v3_folders_create(client):
    """Test case for post_files_v3_folders_create

    Create folder.
    """
    body = {"parentFolderId":"parentFolderId","parentPath":"parentPath","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/files/v3/folders',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_files_v3_folders_update_async_update_properties(client):
    """Test case for post_files_v3_folders_update_async_update_properties

    Update folder properties
    """
    body = {"parentFolderId":0,"name":"name","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/files/v3/folders/update/async',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

