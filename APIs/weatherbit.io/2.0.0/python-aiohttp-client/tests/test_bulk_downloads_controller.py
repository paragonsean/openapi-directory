# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_bulk_files_file_get(client):
    """Test case for bulk_files_file_get

    Download pre-generated bulk datasets
    """
    params = [('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/bulk/files/{file}'.format(file='file_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

