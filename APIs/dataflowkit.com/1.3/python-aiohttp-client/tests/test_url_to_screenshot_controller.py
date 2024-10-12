# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.url2screenshotrequest import Url2screenshotrequest


pytestmark = pytest.mark.asyncio

async def test_url_to_screenshot(client):
    """Test case for url_to_screenshot

    Capture web page Screenshots.
    """
    body = openapi_server.Url2screenshotrequest()
    headers = { 
        'Accept': 'text/plain; charset=utf-8',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/convert/url/screenshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

