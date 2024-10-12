from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def delete_sample_v1_voices_voice_id_samples_sample_id_delete(request: web.Request, voice_id, sample_id, xi_api_key=None) -> web.Response:
    """Delete Sample

    Removes a sample by its ID.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param sample_id: Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
    :type sample_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def get_audio_from_sample_v1_voices_voice_id_samples_sample_id_audio_get(request: web.Request, voice_id, sample_id, xi_api_key=None) -> web.Response:
    """Get Audio From Sample

    Returns the audio corresponding to a sample attached to a voice.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param sample_id: Sample ID to be used, you can use GET https://api.elevenlabs.io/v1/voices/{voice_id} to list all the available samples for a voice.
    :type sample_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)
