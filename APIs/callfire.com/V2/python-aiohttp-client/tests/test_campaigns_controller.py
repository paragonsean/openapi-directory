# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.batch import Batch
from openapi_server.models.call_create_sound import CallCreateSound
from openapi_server.models.campaign_sound import CampaignSound
from openapi_server.models.campaign_sound_page import CampaignSoundPage
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.text_to_speech import TextToSpeech


pytestmark = pytest.mark.asyncio

async def test_delete_campaign_sound(client):
    """Test case for delete_campaign_sound

    Delete a specific sound
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/campaigns/sounds/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_campaign_sounds(client):
    """Test case for find_campaign_sounds

    Find sounds
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('filter', 'filter_example'),
                    ('includeArchived', True),
                    ('includePending', True),
                    ('includeScrubbed', True),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/campaigns/sounds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_batch(client):
    """Test case for get_campaign_batch

    Find a specific batch
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/campaigns/batches/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_sound(client):
    """Test case for get_campaign_sound

    Find a specific sound
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/campaigns/sounds/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_sound_data_mp3(client):
    """Test case for get_campaign_sound_data_mp3

    Download a MP3 sound
    """
    headers = { 
        'Accept': 'audio/mpeg',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/campaigns/sounds/{id_mp}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_sound_data_wav(client):
    """Test case for get_campaign_sound_data_wav

    Download a WAV sound
    """
    headers = { 
        'Accept': 'audio/wav',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/campaigns/sounds/{id_wa}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_call_campaign_sound(client):
    """Test case for post_call_campaign_sound

    Add sound via call
    """
    body = {"name":"name","toNumber":"toNumber"}
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/campaigns/sounds/calls',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_file_campaign_sound(client):
    """Test case for post_file_campaign_sound

    Add sound via file
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v2/campaigns/sounds/files',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_tts_campaign_sound(client):
    """Test case for post_tts_campaign_sound

    Add sound via text-to-speech
    """
    body = {"voice":"MALE1","message":"message"}
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/campaigns/sounds/tts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_campaign_batch(client):
    """Test case for update_campaign_batch

    Update a batch
    """
    body = {"size":9,"broadcastId":5,"created":5,"name":"name","id":2,"enabled":True,"remaining":7,"status":"NEW"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/campaigns/batches/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

