# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.add_voice_response_model import AddVoiceResponseModel
from openapi_server.models.get_voices_response_model import GetVoicesResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.voice_response_model import VoiceResponseModel
from openapi_server.models.voice_settings_response_model import VoiceSettingsResponseModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_add_voice_v1_voices_add_post(client):
    """Test case for add_voice_v1_voices_add_post

    Add Voice
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'xi_api_key': 'xi_api_key_example',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('files', ['/path/to/file'])
    data.add_field('labels', 'labels_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v1/voices/add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_voice_v1_voices_voice_id_delete(client):
    """Test case for delete_voice_v1_voices_voice_id_delete

    Delete Voice
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/voices/{voice_id}'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_voice_settings_v1_voices_voice_id_settings_edit_post(client):
    """Test case for edit_voice_settings_v1_voices_voice_id_settings_edit_post

    Edit Voice Settings
    """
    body = {"similarity_boost":9.301444243932576,"stability":3.616076749251911}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/voices/{voice_id}/settings/edit'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_edit_voice_v1_voices_voice_id_edit_post(client):
    """Test case for edit_voice_v1_voices_voice_id_edit_post

    Edit Voice
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'xi_api_key': 'xi_api_key_example',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('files', ['/path/to/file'])
    data.add_field('labels', 'labels_example')
    data.add_field('name', 'name_example')
    response = await client.request(
        method='POST',
        path='/v1/voices/{voice_id}/edit'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_default_voice_settings_v1_voices_settings_default_get(client):
    """Test case for get_default_voice_settings_v1_voices_settings_default_get

    Get Default Voice Settings.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/voices/settings/default',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_voice_settings_v1_voices_voice_id_settings_get(client):
    """Test case for get_voice_settings_v1_voices_voice_id_settings_get

    Get Voice Settings
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/voices/{voice_id}/settings'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_voice_v1_voices_voice_id_get(client):
    """Test case for get_voice_v1_voices_voice_id_get

    Get Voice
    """
    params = [('with_settings', False)]
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/voices/{voice_id}'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_voices_v1_voices_get(client):
    """Test case for get_voices_v1_voices_get

    Get Voices
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/voices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

