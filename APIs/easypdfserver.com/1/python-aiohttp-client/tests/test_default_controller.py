# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.make_pdf_post_request import MakePdfPostRequest


pytestmark = pytest.mark.asyncio

async def test_make_pdf_post(client):
    """Test case for make_pdf_post

    Generate a PDF from HTML or URL.
    """
    body = openapi_server.MakePdfPostRequest()
    headers = { 
        'Accept': 'application/pdf',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/make-pdf',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

