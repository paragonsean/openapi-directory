# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.share_file_response import ShareFileResponse
from openapi_server.models.tools_share_file_request import ToolsShareFileRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tools_share_file(client):
    """Test case for tools_share_file

    Share file - use to host a file and generate a short link to be used directly in a message or as a link to media for a MMS
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/tools/sharefile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

