# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.upload_media_response import UploadMediaResponse


pytestmark = pytest.mark.asyncio

async def test_delete_media(client):
    """Test case for delete_media

    Delete-Media
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/media/{media_id}'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_media(client):
    """Test case for download_media

    Download-Media
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/media/{media_id}'.format(media_id='media_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_upload_media(client):
    """Test case for upload_media

    Upload-Media
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/msword',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/media',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

