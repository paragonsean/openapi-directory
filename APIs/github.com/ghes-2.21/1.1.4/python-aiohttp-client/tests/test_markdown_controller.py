# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.markdown_render_request import MarkdownRenderRequest


pytestmark = pytest.mark.asyncio

async def test_markdown_render(client):
    """Test case for markdown_render

    Render a Markdown document
    """
    body = openapi_server.MarkdownRenderRequest()
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/markdown',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_markdown_render_raw(client):
    """Test case for markdown_render_raw

    Render a Markdown document in raw mode
    """
    body = 'body_example'
    headers = { 
        'Accept': 'text/html',
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/markdown/raw',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

