# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response200 import InlineResponse200
from openapi_server.models.perfectpdf_api_body import PerfectpdfApiBody


pytestmark = pytest.mark.asyncio

async def test_perfectpdf_api_post(client):
    """Test case for perfectpdf_api_post

    Returns PDF document.
    """
    body = openapi_server.PerfectpdfApiBody()
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/perfectpdf/api',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

