# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_body import ErrorResponseBody


pytestmark = pytest.mark.asyncio

async def test_download_file(client):
    """Test case for download_file

    Download File
    """
    params = [('download', 'download_example'),
                    ('rotation', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/downloads/{dir}/{subdir}/{filename}'.format(subdir='subdir_example', filename='filename_example', dir='dir_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

