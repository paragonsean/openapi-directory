from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch import Batch
from openapi_server.models.call_create_sound import CallCreateSound
from openapi_server.models.campaign_sound import CampaignSound
from openapi_server.models.campaign_sound_page import CampaignSoundPage
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.text_to_speech import TextToSpeech
from openapi_server import util


async def delete_campaign_sound(request: web.Request, id) -> web.Response:
    """Delete a specific sound

    Deletes a single campaign sound instance for a specific campaign sound id, this operation does not delete sound completely, it sets sound status to ARCHIVED which means that sound will no longer appear in &#39;find&#39; operation results, but still accessible via &#39;get&#39; operation

    :param id: An id of a campaign sound
    :type id: int

    """
    return web.Response(status=200)


async def find_campaign_sounds(request: web.Request, limit=None, offset=None, filter=None, include_archived=None, include_pending=None, include_scrubbed=None, fields=None) -> web.Response:
    """Find sounds

    To find all campaign sounds which were created by user. Returns all sounds available to be used in campaigns

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param filter: value to filter file names again; this value is used to check if the filename contains the filter value.
    :type filter: str
    :param include_archived: Includes ARCHIVED sounds for \&quot;true\&quot; value
    :type include_archived: bool
    :param include_pending: Includes UPLOAD/RECORDING sounds for \&quot;true\&quot; value
    :type include_pending: bool
    :param include_scrubbed: Includes SCRUBBED sounds for \&quot;true\&quot; value
    :type include_scrubbed: bool
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_campaign_batch(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific batch

    Returns a single Batch instance for a given batch id. This API is useful for determining the state of a validating batch

    :param id: An id of a batch
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_campaign_sound(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific sound

    Returns a single CampaignSound instance for a given sound id in campaign. This is a meta data to the sounds. No audio data is returned from this API

    :param id: An id of a sound campaign
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_campaign_sound_data_mp3(request: web.Request, id) -> web.Response:
    """Download a MP3 sound

    Download the MP3 version of a hosted file. This is an audio data endpoint. Returns binary response of the &#39;audio/mpeg&#39; content type

    :param id: An id of a campaign sound
    :type id: int

    """
    return web.Response(status=200)


async def get_campaign_sound_data_wav(request: web.Request, id) -> web.Response:
    """Download a WAV sound

    Download the WAV version of the hosted file. This is an audio data endpoint. Returns binary response of the &#39;audio/mpeg&#39; content type

    :param id: An id of a campaign sound
    :type id: int

    """
    return web.Response(status=200)


async def post_call_campaign_sound(request: web.Request, fields=None, body=None) -> web.Response:
    """Add sound via call

    Use this API to create a sound via a phone call. Provide the required phone number in the CallCreateSound object inside the request, and user will receive a call shortly after with instructions on how to record a sound over the phone.

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param body: Request object containing the name of a new campaign sound and phone number to call up
    :type body: dict | bytes

    """
    body = CallCreateSound.from_dict(body)
    return web.Response(status=200)


async def post_file_campaign_sound(request: web.Request, file, fields=None, name=None) -> web.Response:
    """Add sound via file

    Create a campaign sound file via a supplied .mp3 or .wav file

    :param file: A sound file encoded in binary form
    :type file: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param name: Optional name of a sound file, if the name is empty than it will be taken from a file
    :type name: str

    """
    return web.Response(status=200)


async def post_tts_campaign_sound(request: web.Request, fields=None, body=None) -> web.Response:
    """Add sound via text-to-speech

    Use this API to create a sound file via a supplied string of text. Add a text in the TextToSpeech.message field, and pick a voice in the TextToSpeech.voice field. Available voices are: MALE1, FEMALE1, FEMALE2, SPANISH1, FRENCHCANADIAN1

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param body: textToSpeech
    :type body: dict | bytes

    """
    body = TextToSpeech.from_dict(body)
    return web.Response(status=200)


async def update_campaign_batch(request: web.Request, id, body=None) -> web.Response:
    """Update a batch

    Updates a single Batch instance, currently batch can only be turned \&quot;on/off\&quot;

    :param id: An id of a batch to update
    :type id: int
    :param body: A batch instance
    :type body: dict | bytes

    """
    body = Batch.from_dict(body)
    return web.Response(status=200)
