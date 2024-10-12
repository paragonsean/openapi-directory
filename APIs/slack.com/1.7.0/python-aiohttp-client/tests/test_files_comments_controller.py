# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.files_comments_delete_error_schema import FilesCommentsDeleteErrorSchema
from openapi_server.models.files_comments_delete_schema import FilesCommentsDeleteSchema


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_files_comments_delete(client):
    """Test case for files_comments_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'file': 'file_example',
        'id': 'id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/files.comments.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

