# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_delete_sample_v1_voices_voice_id_samples_sample_id_delete(client):
    """Test case for delete_sample_v1_voices_voice_id_samples_sample_id_delete

    Delete Sample
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/voices/{voice_id}/samples/{sample_id}'.format(voice_id='21m00Tcm4TlvDq8ikWAM', sample_id='VW7YKqPnjY4h39yTbx2L'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get(client):
    """Test case for get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get

    Get Audio From Sample
    """
    headers = { 
        'Accept': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/v1/voices/{voice_id}/samples/{sample_id}/audio'.format(voice_id='21m00Tcm4TlvDq8ikWAM', sample_id='VW7YKqPnjY4h39yTbx2L'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

