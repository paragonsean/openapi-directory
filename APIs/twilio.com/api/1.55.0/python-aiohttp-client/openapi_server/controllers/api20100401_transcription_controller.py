from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_recording_recording_transcription import ApiV2010AccountRecordingRecordingTranscription
from openapi_server.models.api_v2010_account_transcription import ApiV2010AccountTranscription
from openapi_server.models.list_recording_transcription_response import ListRecordingTranscriptionResponse
from openapi_server.models.list_transcription_response import ListTranscriptionResponse
from openapi_server import util


async def delete_recording_transcription(request: web.Request, account_sid, recording_sid, sid) -> web.Response:
    """delete_recording_transcription

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete.
    :type account_sid: str
    :param recording_sid: The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to delete.
    :type recording_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def delete_transcription(request: web.Request, account_sid, sid) -> web.Response:
    """delete_transcription

    Delete a transcription from the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_recording_transcription(request: web.Request, account_sid, recording_sid, sid) -> web.Response:
    """fetch_recording_transcription

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.
    :type account_sid: str
    :param recording_sid: The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcription to fetch.
    :type recording_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_transcription(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_transcription

    Fetch an instance of a Transcription

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_recording_transcription(request: web.Request, account_sid, recording_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_recording_transcription

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.
    :type account_sid: str
    :param recording_sid: The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) that created the transcriptions to read.
    :type recording_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def list_transcription(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_transcription

    Retrieve a list of transcriptions belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
