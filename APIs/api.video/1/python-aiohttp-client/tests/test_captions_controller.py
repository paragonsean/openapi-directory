# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.captions_list_response import CaptionsListResponse
from openapi_server.models.captions_update_payload import CaptionsUpdatePayload
from openapi_server.models.not_found import NotFound
from openapi_server.models.subtitle import Subtitle


pytestmark = pytest.mark.asyncio

async def test_d_elete_videos_video_id_captions_language(client):
    """Test case for d_elete_videos_video_id_captions_language

    Delete a caption
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/captions/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklgc', language='en'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_videos_video_id_captions(client):
    """Test case for g_et_videos_video_id_captions

    List video captions
    """
    params = [('currentPage', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/captions'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_g_et_videos_video_id_captions_language(client):
    """Test case for g_et_videos_video_id_captions_language

    Show a caption
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/captions/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklg', language='en'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p_atch_videos_video_id_captions_language(client):
    """Test case for p_atch_videos_video_id_captions_language

    Update caption
    """
    body = openapi_server.CaptionsUpdatePayload()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/captions/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklg', language='en'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_p_ost_videos_video_id_captions_language(client):
    """Test case for p_ost_videos_video_id_captions_language

    Upload a caption
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
        path='/videos/{video_id}/captions/{language}'.format(video_id='vi4k0jvEUuaTdRAEjQ4Prklg', language='en'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

