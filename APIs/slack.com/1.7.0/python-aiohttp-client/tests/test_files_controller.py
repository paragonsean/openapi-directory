# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server.models.files_comments_delete_error_schema import FilesCommentsDeleteErrorSchema
from openapi_server.models.files_comments_delete_schema import FilesCommentsDeleteSchema
from openapi_server.models.files_delete_error_schema import FilesDeleteErrorSchema
from openapi_server.models.files_delete_schema import FilesDeleteSchema
from openapi_server.models.files_info_error_schema import FilesInfoErrorSchema
from openapi_server.models.files_info_schema import FilesInfoSchema
from openapi_server.models.files_list_error_schema import FilesListErrorSchema
from openapi_server.models.files_list_schema import FilesListSchema
from openapi_server.models.files_revoke_public_url_error_schema import FilesRevokePublicURLErrorSchema
from openapi_server.models.files_revoke_public_url_schema import FilesRevokePublicURLSchema
from openapi_server.models.files_shared_public_url_error_schema import FilesSharedPublicURLErrorSchema
from openapi_server.models.files_shared_public_url_schema import FilesSharedPublicURLSchema
from openapi_server.models.files_upload_error_schema import FilesUploadErrorSchema
from openapi_server.models.files_upload_schema import FilesUploadSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_comments_delete_0(client):
    """Test case for files_comments_delete_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'file': 'file_example',
        'id': 'id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.comments.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_delete(client):
    """Test case for files_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'file': 'file_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_info(client):
    """Test case for files_info

    
    """
    params = [('token', 'token_example'),
                    ('file', 'file_example'),
                    ('count', 'count_example'),
                    ('page', 'page_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/files.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_list(client):
    """Test case for files_list

    
    """
    params = [('token', 'token_example'),
                    ('user', 'user_example'),
                    ('channel', 'channel_example'),
                    ('ts_from', 3.4),
                    ('ts_to', 3.4),
                    ('types', 'types_example'),
                    ('count', 'count_example'),
                    ('page', 'page_example'),
                    ('show_files_hidden_by_limit', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/files.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_remote_add_0(client):
    """Test case for files_remote_add_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'external_id': 'external_id_example',
        'external_url': 'external_url_example',
        'filetype': 'filetype_example',
        'indexable_file_contents': 'indexable_file_contents_example',
        'preview_image': 'preview_image_example',
        'title': 'title_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.remote.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_remote_info_0(client):
    """Test case for files_remote_info_0

    
    """
    params = [('token', 'token_example'),
                    ('file', 'file_example'),
                    ('external_id', 'external_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/files.remote.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_remote_list_0(client):
    """Test case for files_remote_list_0

    
    """
    params = [('token', 'token_example'),
                    ('channel', 'channel_example'),
                    ('ts_from', 3.4),
                    ('ts_to', 3.4),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/files.remote.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_remote_remove_0(client):
    """Test case for files_remote_remove_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'external_id': 'external_id_example',
        'file': 'file_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.remote.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_remote_share_0(client):
    """Test case for files_remote_share_0

    
    """
    params = [('token', 'token_example'),
                    ('file', 'file_example'),
                    ('external_id', 'external_id_example'),
                    ('channels', 'channels_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/files.remote.share',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_remote_update_0(client):
    """Test case for files_remote_update_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'external_id': 'external_id_example',
        'external_url': 'external_url_example',
        'file': 'file_example',
        'filetype': 'filetype_example',
        'indexable_file_contents': 'indexable_file_contents_example',
        'preview_image': 'preview_image_example',
        'title': 'title_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.remote.update',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_revoke_public_url(client):
    """Test case for files_revoke_public_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'file': 'file_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.revokePublicURL',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_shared_public_url(client):
    """Test case for files_shared_public_url

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'file': 'file_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.sharedPublicURL',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_upload(client):
    """Test case for files_upload

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channels': 'channels_example',
        'content': 'content_example',
        'file': 'file_example',
        'filename': 'filename_example',
        'filetype': 'filetype_example',
        'initial_comment': 'initial_comment_example',
        'thread_ts': 3.4,
        'title': 'title_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

