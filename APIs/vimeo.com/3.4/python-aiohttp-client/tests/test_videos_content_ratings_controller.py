# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_rating import ContentRating


pytestmark = pytest.mark.asyncio

async def test_get_content_ratings(client):
    """Test case for get_content_ratings

    Get all content ratings
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.contentrating+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/contentratings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

