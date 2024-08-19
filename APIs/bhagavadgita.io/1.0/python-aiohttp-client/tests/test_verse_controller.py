# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.verse_schema import VerseSchema


pytestmark = pytest.mark.asyncio

async def test_api_v1_chapters_chapter_number_verses_get(client):
    """Test case for api_v1_chapters_chapter_number_verses_get

    Get all the Verses from a Chapter.
    """
    params = [('access_token', 'access_token_example'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/chapters/{chapter_number}/verses'.format(chapter_number=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_chapters_chapter_number_verses_verse_number_get(client):
    """Test case for api_v1_chapters_chapter_number_verses_verse_number_get

    Get a particular verse from a chapter.
    """
    params = [('access_token', 'access_token_example'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/chapters/{chapter_number}/verses/{verse_number}'.format(chapter_number=1, verse_number=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_v1_verses_get(client):
    """Test case for api_v1_verses_get

    Get all the Verses.
    """
    params = [('access_token', 'access_token_example'),
                    ('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/verses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

