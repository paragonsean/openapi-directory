# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chapter_schema import ChapterSchema


pytestmark = pytest.mark.asyncio

async def test_api_v1_chapters_chapter_number_get(client):
    """Test case for api_v1_chapters_chapter_number_get

    Get a specific chapter from the Bhagavad Gita.
    """
    params = [('access_token', 'access_token_example'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/chapters/{chapter_number}'.format(chapter_number=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_chapters_get(client):
    """Test case for api_v1_chapters_get

    Get all the 18 Chapters of the Bhagavad Gita.
    """
    params = [('access_token', 'access_token_example'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/chapters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

