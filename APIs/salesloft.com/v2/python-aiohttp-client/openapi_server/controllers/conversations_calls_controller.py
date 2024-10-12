from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversations_call import ConversationsCall
from openapi_server import util


async def v2_conversations_calls_post(request: web.Request, duration, _from, recording, to, call_created_at=None, direction=None, user_guid=None) -> web.Response:
    """Create Conversations Call

    Enqueue a Conversations Call for processing

    :param duration: Duration of call in seconds
    :type duration: 
    :param _from: Phone number that call was made from
    :type _from: str
    :param recording: Object containing recording info including the audio file (.mp3, .wav, .ogg, .m4a)
    :type recording: dict | bytes
    :param to:  Phone number that was called
    :type to: str
    :param call_created_at: Timestamp for when the call started. If not provided, will default to the time the request was received
    :type call_created_at: str
    :param direction: Call direction
    :type direction: str
    :param user_guid: Guid of the Salesloft User to assign the call to. If not provided, will default to the user within the authentication token
    :type user_guid: str

    """
    recording = object.from_dict(recording)
    return web.Response(status=200)
