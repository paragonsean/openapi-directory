from typing import List, Dict
from aiohttp import web

from openapi_server.models.body_text_to_speech_v1_text_to_speech_voice_id_post import BodyTextToSpeechV1TextToSpeechVoiceIdPost
from openapi_server.models.body_text_to_speech_v1_text_to_speech_voice_id_stream_post import BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def text_to_speech_v1_text_to_speech_voice_id_post(request: web.Request, voice_id, body, xi_api_key=None) -> web.Response:
    """Text To Speech

    Converts text into speech using a voice of your choice and returns audio.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param body: 
    :type body: dict | bytes
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    body = BodyTextToSpeechV1TextToSpeechVoiceIdPost.from_dict(body)
    return web.Response(status=200)


async def text_to_speech_v1_text_to_speech_voice_id_stream_post(request: web.Request, voice_id, body, xi_api_key=None) -> web.Response:
    """Text To Speech

    Converts text into speech using a voice of your choice and returns audio as an audio stream.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param body: 
    :type body: dict | bytes
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    body = BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost.from_dict(body)
    return web.Response(status=200)
