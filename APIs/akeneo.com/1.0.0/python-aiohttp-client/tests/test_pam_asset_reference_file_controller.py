# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_reference_files_locale_code200_response import GetReferenceFilesLocaleCode200Response
from openapi_server.models.post_reference_files_locale_code201_response import PostReferenceFilesLocaleCode201Response
from openapi_server.models.post_reference_files_locale_code_request import PostReferenceFilesLocaleCodeRequest
from openapi_server.models.post_token400_response import PostToken400Response


pytestmark = pytest.mark.asyncio

async def test_get_reference_files_channel_code_locale_code_download(client):
    """Test case for get_reference_files_channel_code_locale_code_download

    Download a reference file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/assets/{asset_code}/reference-files/{locale_code}/download'.format(asset_code='asset_code_example', locale_code='locale_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_files_locale_code(client):
    """Test case for get_reference_files_locale_code

    Get a reference file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/assets/{asset_code}/reference-files/{locale_code}'.format(asset_code='asset_code_example', locale_code='locale_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_post_reference_files_locale_code(client):
    """Test case for post_reference_files_locale_code

    Upload a new reference file
    """
    body = openapi_server.PostReferenceFilesLocaleCodeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/assets/{asset_code}/reference-files/{locale_code}'.format(asset_code='asset_code_example', locale_code='locale_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

