# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chapter_object import ChapterObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_several_chapters200_response import GetSeveralChapters200Response
from openapi_server.models.paging_simplified_chapter_object import PagingSimplifiedChapterObject


pytestmark = pytest.mark.asyncio

async def test_get_a_chapter(client):
    """Test case for get_a_chapter

    Get a Chapter 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/chapters/{id}'.format(id='0D5wENdkdwbqlrHoaJ9g29'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audiobook_chapters_0(client):
    """Test case for get_audiobook_chapters_0

    Get Audiobook Chapters 
    """
    params = [('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audiobooks/{id}/chapters'.format(id='7iHfbu1YPACw6oZPAFJtqe'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_several_chapters(client):
    """Test case for get_several_chapters

    Get Several Chapters 
    """
    params = [('ids', '0IsXVP0JmcB2adSE338GkK,3ZXb8FKZGU0EHALYX6uCzU,0D5wENdkdwbqlrHoaJ9g29'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/chapters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

