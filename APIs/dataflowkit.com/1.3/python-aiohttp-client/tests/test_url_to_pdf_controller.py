# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.url2pdfrequest import Url2pdfrequest


pytestmark = pytest.mark.asyncio

async def test_url_to_pdf(client):
    """Test case for url_to_pdf

    Save web page as PDF
    """
    body = openapi_server.Url2pdfrequest()
    headers = { 
        'Accept': 'text/plain; charset=utf-8',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/convert/url/pdf',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

