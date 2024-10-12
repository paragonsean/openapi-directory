# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.post_asset_media_files_request import PostAssetMediaFilesRequest
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_asset_media_files_code(client):
    """Test case for get_asset_media_files_code

    Download the media file associated to an asset
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/asset-media-files/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_asset_media_files(client):
    """Test case for post_asset_media_files

    Create a new media file for an asset
    """
    body = openapi_server.PostAssetMediaFilesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/asset-media-files',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

