# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.collection_response_file import CollectionResponseFile
from openapi_server.models.error import Error
from openapi_server.models.file import File
from openapi_server.models.file_action_response import FileActionResponse
from openapi_server.models.file_stat import FileStat
from openapi_server.models.file_update_input import FileUpdateInput
from openapi_server.models.import_from_url_input import ImportFromUrlInput
from openapi_server.models.import_from_url_task_locator import ImportFromUrlTaskLocator
from openapi_server.models.signed_url import SignedUrl


pytestmark = pytest.mark.asyncio

async def test_delete_files_v3_files_file_id_archive(client):
    """Test case for delete_files_v3_files_file_id_archive

    Delete file
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_files_v3_files_file_id_gdpr_delete_archive_gdpr(client):
    """Test case for delete_files_v3_files_file_id_gdpr_delete_archive_gdpr

    GDPR delete
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/files/v3/files/{file_id}/gdpr-delete'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_files_file_id_get_by_id(client):
    """Test case for get_files_v3_files_file_id_get_by_id

    Get file.
    """
    params = [('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_files_file_id_signed_url_get_signed_url(client):
    """Test case for get_files_v3_files_file_id_signed_url_get_signed_url

    Get signed URL to access private file.
    """
    params = [('size', 'size_example'),
                    ('expirationSeconds', 56),
                    ('upscale', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/files/{file_id}/signed-url'.format(file_id='file_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_files_import_from_url_async_tasks_task_id_status_check_import(client):
    """Test case for get_files_v3_files_import_from_url_async_tasks_task_id_status_check_import

    Check import status.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/files/import-from-url/async/tasks/{task_id}/status'.format(task_id='task_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_files_search_do_search(client):
    """Test case for get_files_v3_files_search_do_search

    Search files
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
                    ('parentFolderId', 56),
                    ('size', 56),
                    ('height', 56),
                    ('width', 56),
                    ('encoding', 'encoding_example'),
                    ('type', 'type_example'),
                    ('extension', 'extension_example'),
                    ('url', 'url_example'),
                    ('isUsableInContent', True),
                    ('allowsAnonymousAccess', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/files/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files_v3_files_stat_path_get_metadata(client):
    """Test case for get_files_v3_files_stat_path_get_metadata

    
    """
    params = [('properties', ['properties_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/files/v3/files/stat/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_files_v3_files_file_id_update_properties(client):
    """Test case for patch_files_v3_files_file_id_update_properties

    update file properties
    """
    body = {"access":"PUBLIC_INDEXABLE","parentFolderId":"parentFolderId","name":"name","parentFolderPath":"parentFolderPath","isUsableInContent":True,"expiresAt":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/files/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_files_v3_files_import_from_url_async_import_from_url(client):
    """Test case for post_files_v3_files_import_from_url_async_import_from_url

    Import a file from a URL into the file manager.
    """
    body = {"folderPath":"folderPath","access":"PUBLIC_INDEXABLE","duplicateValidationScope":"ENTIRE_PORTAL","name":"name","duplicateValidationStrategy":"NONE","overwrite":True,"ttl":"ttl","folderId":"folderId","url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/files/v3/files/import-from-url/async',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_files_v3_files_upload(client):
    """Test case for post_files_v3_files_upload

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    data = FormData()
    data.add_field('charset_hunch', 'charset_hunch_example')
    data.add_field('file', '/path/to/file')
    data.add_field('file_name', 'file_name_example')
    data.add_field('folder_id', 'folder_id_example')
    data.add_field('folder_path', 'folder_path_example')
    data.add_field('options', 'options_example')
    response = await client.request(
        method='POST',
        path='/files/v3/files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_put_files_v3_files_file_id_replace(client):
    """Test case for put_files_v3_files_file_id_replace

    Replace file.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    data = FormData()
    data.add_field('charset_hunch', 'charset_hunch_example')
    data.add_field('file', '/path/to/file')
    data.add_field('options', 'options_example')
    response = await client.request(
        method='PUT',
        path='/files/v3/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

