# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.document_block_list import DocumentBlockList
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse


pytestmark = pytest.mark.asyncio

async def test_list_document_block(client):
    """Test case for list_document_block

    List all document blocks
    """
    params = [('page', 56),
                    ('per_page', 25)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/document-blocks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

