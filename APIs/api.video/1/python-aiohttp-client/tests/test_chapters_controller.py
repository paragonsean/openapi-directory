# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.chapter import Chapter
from openapi_server.models.chapters_list_response import ChaptersListResponse
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_d_elete_videos_video_id_chapters_language(client):
    """Test case for d_elete_videos_video_id_chapters_language

    Delete a chapter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/chapters/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz', language='en'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_videos_video_id_chapters(client):
    """Test case for g_et_videos_video_id_chapters

    List video chapters
    """
    params = [('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/chapters'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_videos_video_id_chapters_language(client):
    """Test case for g_et_videos_video_id_chapters_language

    Show a chapter
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/chapters/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz', language='en'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_videos_video_id_chapters_language(client):
    """Test case for p_ost_videos_video_id_chapters_language

    Upload a chapter
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/chapters/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Jfrgz', language='en'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

