# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Uploads a temporary file (ie. for XML import). Returns token which can be used in other API calls.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/home-api/files',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

