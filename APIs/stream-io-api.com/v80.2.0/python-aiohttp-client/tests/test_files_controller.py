# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_error import APIError
from openapi_server.models.file_delete_response import FileDeleteResponse
from openapi_server.models.file_upload_response import FileUploadResponse
from openapi_server.models.image_size_request import ImageSizeRequest
from openapi_server.models.image_upload_response import ImageUploadResponse
from openapi_server.models.only_user_id_request import OnlyUserIDRequest


pytestmark = pytest.mark.asyncio

async def test_delete_file_0(client):
    """Test case for delete_file_0

    Delete file
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{type}/{id}/file'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_0(client):
    """Test case for delete_image_0

    Delete image
    """
    params = [('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/channels/{type}/{id}/image'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file_0(client):
    """Test case for upload_file_0

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    data = FormData()
    data.add_field('file', 'file_example')
    data.add_field('user', openapi_server.OnlyUserIDRequest())
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/file'.format(type='type_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_image_0(client):
    """Test case for upload_image_0

    Upload image
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    data = FormData()
    data.add_field('file', 'file_example')
    data.add_field('upload_sizes', [openapi_server.ImageSizeRequest()])
    data.add_field('user', openapi_server.OnlyUserIDRequest())
    response = await client.request(
        method='POST',
        path='/channels/{type}/{id}/image'.format(type='type_example', id='id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

