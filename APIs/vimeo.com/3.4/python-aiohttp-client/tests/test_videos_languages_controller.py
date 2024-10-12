# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.language import Language


pytestmark = pytest.mark.asyncio

async def test_get_languages(client):
    """Test case for get_languages

    Get all languages
    """
    params = [('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.language+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/languages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

