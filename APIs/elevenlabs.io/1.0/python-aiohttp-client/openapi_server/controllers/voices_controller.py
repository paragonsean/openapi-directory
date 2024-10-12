from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_voice_response_model import AddVoiceResponseModel
from openapi_server.models.get_voices_response_model import GetVoicesResponseModel
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.voice_response_model import VoiceResponseModel
from openapi_server.models.voice_settings_response_model import VoiceSettingsResponseModel
from openapi_server import util


async def add_voice_v1_voices_add_post(request: web.Request, files, name, xi_api_key=None, description=None, labels=None) -> web.Response:
    """Add Voice

    Add a new voice to your collection of voices in VoiceLab.

    :param files: One or more audio files to clone the voice from
    :type files: List[str]
    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type name: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str
    :param description: How would you describe the voice?
    :type description: str
    :param labels: Serialized labels dictionary for the voice.
    :type labels: str

    """
    return web.Response(status=200)


async def delete_voice_v1_voices_voice_id_delete(request: web.Request, voice_id, xi_api_key=None) -> web.Response:
    """Delete Voice

    Deletes a voice by its ID.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def edit_voice_settings_v1_voices_voice_id_settings_edit_post(request: web.Request, voice_id, body, xi_api_key=None) -> web.Response:
    """Edit Voice Settings

    Edit your settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param body: 
    :type body: dict | bytes
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    body = VoiceSettingsResponseModel.from_dict(body)
    return web.Response(status=200)


async def edit_voice_v1_voices_voice_id_edit_post(request: web.Request, voice_id, name, xi_api_key=None, description=None, files=None, labels=None) -> web.Response:
    """Edit Voice

    Edit a voice created by you.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param name: The name that identifies this voice. This will be displayed in the dropdown of the website.
    :type name: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str
    :param description: How would you describe the voice?
    :type description: str
    :param files: Audio files to add to the voice
    :type files: List[str]
    :param labels: Serialized labels dictionary for the voice.
    :type labels: str

    """
    return web.Response(status=200)


async def get_default_voice_settings_v1_voices_settings_default_get(request: web.Request, ) -> web.Response:
    """Get Default Voice Settings.

    Gets the default settings for voices. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.


    """
    return web.Response(status=200)


async def get_voice_settings_v1_voices_voice_id_settings_get(request: web.Request, voice_id, xi_api_key=None) -> web.Response:
    """Get Voice Settings

    Returns the settings for a specific voice. \&quot;similarity_boost\&quot; corresponds to\&quot;Clarity + Similarity Enhancement\&quot; in the web app and \&quot;stability\&quot; corresponds to \&quot;Stability\&quot; slider in the web app.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def get_voice_v1_voices_voice_id_get(request: web.Request, voice_id, with_settings=None, xi_api_key=None) -> web.Response:
    """Get Voice

    Returns metadata about a specific voice.

    :param voice_id: Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.
    :type voice_id: str
    :param with_settings: If set will return settings information corresponding to the voice, requires authorization.
    :type with_settings: bool
    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)


async def get_voices_v1_voices_get(request: web.Request, xi_api_key=None) -> web.Response:
    """Get Voices

    Gets a list of all available voices for a user.

    :param xi_api_key: Your API key. This is required by most endpoints to access our API programatically. You can view your xi-api-key using the &#39;Profile&#39; tab on the website.
    :type xi_api_key: str

    """
    return web.Response(status=200)
