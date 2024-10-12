# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_failure import ApiResponseFailure
from openapi_server.models.api_response_success import ApiResponseSuccess
from openapi_server.models.merge_request import MergeRequest


pytestmark = pytest.mark.asyncio

async def test_merge_post(client):
    """Test case for merge_post

    Merge multiple PDFs together
    """
    body = {"fileName":"test.pdf","urls":["link-to-pdf1","link-to-pdf2","link-to-pdf3"],"inlinePdf":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/merge',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

