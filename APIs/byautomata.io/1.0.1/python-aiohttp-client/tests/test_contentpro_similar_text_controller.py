# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contentpro_search_get200_response import ContentproSearchGet200Response
from openapi_server.models.contentpro_similar_text_post_request import ContentproSimilarTextPostRequest


pytestmark = pytest.mark.asyncio

async def test_contentpro_similar_text_post(client):
    """Test case for contentpro_similar_text_post

    The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies.
    """
    body = openapi_server.ContentproSimilarTextPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/contentpro-similar-text',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

