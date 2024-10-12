# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.preview_response import PreviewResponse


pytestmark = pytest.mark.asyncio

async def test_previews_read(client):
    """Test case for previews_read

    Get preview image of uploaded file
    """
    headers = { 
        'Accept': 'application/json',
        'Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-v1/previews/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

