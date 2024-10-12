# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.body_text_to_speech_v1_text_to_speech_voice_id_post import BodyTextToSpeechV1TextToSpeechVoiceIdPost
from openapi_server.models.body_text_to_speech_v1_text_to_speech_voice_id_stream_post import BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_text_to_speech_v1_text_to_speech_voice_id_post(client):
    """Test case for text_to_speech_v1_text_to_speech_voice_id_post

    Text To Speech
    """
    body = openapi_server.BodyTextToSpeechV1TextToSpeechVoiceIdPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/text-to-speech/{voice_id}'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_text_to_speech_v1_text_to_speech_voice_id_stream_post(client):
    """Test case for text_to_speech_v1_text_to_speech_voice_id_stream_post

    Text To Speech
    """
    body = openapi_server.BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xi_api_key': 'xi_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/v1/text-to-speech/{voice_id}/stream'.format(voice_id='21m00Tcm4TlvDq8ikWAM'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

