# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.endpoint_get_markdown_emoticons import EndpointGetMarkdownEmoticons
from openapi_server.models.endpoint_post_markdown import EndpointPostMarkdown


pytestmark = pytest.mark.asyncio

async def test_markdown_emoticons_get(client):
    """Test case for markdown_emoticons_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/markdown/emoticons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_markdown_post(client):
    """Test case for markdown_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('text_emoticons', False)
    data.add_field('text_raw', 'text_raw_example')
    response = await client.request(
        method='POST',
        path='/connect/api/v4/markdown',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

