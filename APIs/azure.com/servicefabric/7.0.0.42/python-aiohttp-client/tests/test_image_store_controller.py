# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.folder_size_info import FolderSizeInfo
from openapi_server.models.image_store_content import ImageStoreContent
from openapi_server.models.image_store_copy_description import ImageStoreCopyDescription
from openapi_server.models.image_store_info import ImageStoreInfo
from openapi_server.models.upload_session import UploadSession


pytestmark = pytest.mark.asyncio

async def test_commit_image_store_upload_session(client):
    """Test case for commit_image_store_upload_session

    Commit an image store upload session.
    """
    params = [('api-version', 6.0),
                    ('session-id', 'session_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ImageStore/$/CommitUploadSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_copy_image_store_content(client):
    """Test case for copy_image_store_content

    Copies image store content internally
    """
    image_store_copy_description = openapi_server.ImageStoreCopyDescription()
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ImageStore/$/Copy',
        headers=headers,
        json=image_store_copy_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_store_content(client):
    """Test case for delete_image_store_content

    Deletes existing image store content.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/ImageStore/{content_path}'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_store_upload_session(client):
    """Test case for delete_image_store_upload_session

    Cancels an image store upload session.
    """
    params = [('api-version', 6.0),
                    ('session-id', 'session_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/ImageStore/$/DeleteUploadSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_content(client):
    """Test case for get_image_store_content

    Gets the image store content information.
    """
    params = [('api-version', 6.2),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/{content_path}'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_folder_size(client):
    """Test case for get_image_store_folder_size

    Get the size of a folder in image store
    """
    params = [('api-version', 6.5),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/{content_path}/$/FolderSize'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_info(client):
    """Test case for get_image_store_info

    Gets the overall ImageStore information
    """
    params = [('api-version', 6.5),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/$/Info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_root_content(client):
    """Test case for get_image_store_root_content

    Gets the content information at the root of the image store.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_root_folder_size(client):
    """Test case for get_image_store_root_folder_size

    Get the folder size at the root of the image store.
    """
    params = [('api-version', 6.5),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/$/FolderSize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_upload_session_by_id(client):
    """Test case for get_image_store_upload_session_by_id

    Get the image store upload session by ID.
    """
    params = [('api-version', 6.0),
                    ('session-id', 'session_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/$/GetUploadSession',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_store_upload_session_by_path(client):
    """Test case for get_image_store_upload_session_by_path

    Get the image store upload session by relative path.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ImageStore/{content_path}/$/GetUploadSession'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_file(client):
    """Test case for upload_file

    Uploads contents of the file to the image store.
    """
    params = [('api-version', 6.0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ImageStore/{content_path}'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upload_file_chunk(client):
    """Test case for upload_file_chunk

    Uploads a file chunk to the image store relative path.
    """
    params = [('api-version', 6.0),
                    ('session-id', 'session_id_example'),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'content_range': 'content_range_example',
    }
    response = await client.request(
        method='PUT',
        path='/ImageStore/{content_path}/$/UploadChunk'.format(content_path='content_path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

