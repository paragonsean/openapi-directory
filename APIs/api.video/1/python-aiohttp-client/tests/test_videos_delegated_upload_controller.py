# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.not_found import NotFound
from openapi_server.models.token_create_payload import TokenCreatePayload
from openapi_server.models.token_list_response import TokenListResponse
from openapi_server.models.upload_token import UploadToken
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_d_elete_upload_tokens_upload_token(client):
    """Test case for d_elete_upload_tokens_upload_token

    Delete an upload token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/upload-tokens/{upload_token}'.format(upload_token='to1tcmSFHeYY5KzyhOqVKMKb'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_upload_tokens(client):
    """Test case for g_et_upload_tokens

    List all active upload tokens.
    """
    params = [('sortBy', 'ttl'),
                    ('sortOrder', 'asc'),
                    ('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/upload-tokens',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_upload_tokens_upload_token(client):
    """Test case for g_et_upload_tokens_upload_token

    Show upload token
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/upload-tokens/{upload_token}'.format(upload_token='to1tcmSFHeYY5KzyhOqVKMKb'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_upload(client):
    """Test case for p_ost_upload

    Upload with an upload token
    """
    params = [('token', 'to1tcmSFHeYY5KzyhOqVKMKb')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_range': 'Content-Range: bytes 200-100/5000',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('video_id', 'video_id_example')
    response = await client.request(
        method='POST',
        path='/upload',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_ost_upload_tokens(client):
    """Test case for p_ost_upload_tokens

    Generate an upload token
    """
    body = openapi_server.TokenCreatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/upload-tokens',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

