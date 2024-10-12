# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_download_avatar(client):
    """Test case for download_avatar

    Download avatar
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/downloads/avatar/{user_id}/{uuid}'.format(user_id=56, uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_file_via_token(client):
    """Test case for download_file_via_token

    Download file
    """
    params = [('generic_mimetype', True),
                    ('inline', True)]
    headers = { 
        'Accept': 'application/octet-stream',
        'range': 'range_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/downloads/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_file_via_token1(client):
    """Test case for download_file_via_token1

    Download file
    """
    params = [('generic_mimetype', True),
                    ('inline', True)]
    headers = { 
        'Accept': 'application/octet-stream',
        'range': 'range_example',
    }
    response = await client.request(
        method='HEAD',
        path='/api/v4/downloads/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_zip_archive_via_token(client):
    """Test case for download_zip_archive_via_token

    Download ZIP archive
    """
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/downloads/zip/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

