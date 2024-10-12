# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_remote_add(client):
    """Test case for files_remote_add

    
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

async def test_files_remote_info(client):
    """Test case for files_remote_info

    
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

async def test_files_remote_list(client):
    """Test case for files_remote_list

    
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
async def test_files_remote_remove(client):
    """Test case for files_remote_remove

    
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

async def test_files_remote_share(client):
    """Test case for files_remote_share

    
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
async def test_files_remote_update(client):
    """Test case for files_remote_update

    
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

