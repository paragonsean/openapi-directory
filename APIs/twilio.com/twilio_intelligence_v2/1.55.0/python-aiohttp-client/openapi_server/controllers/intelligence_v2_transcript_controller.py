from typing import List, Dict
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript import IntelligenceV2Transcript
from openapi_server.models.list_transcript_response import ListTranscriptResponse
from openapi_server import util


async def create_transcript(request: web.Request, channel, service_sid, customer_key=None, media_start_time=None) -> web.Response:
    """create_transcript

    Create a new Transcript for the service

    :param channel: JSON object describing Media Channel including Source and Participants
    :type channel: dict | bytes
    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param customer_key: Used to store client provided metadata. Maximum of 64 double-byte UTF8 characters.
    :type customer_key: str
    :param media_start_time: The date that this Transcript&#39;s media was started, given in ISO 8601 format.
    :type media_start_time: str

    """
    channel = object.from_dict(channel)
    media_start_time = util.deserialize_datetime(media_start_time)
    return web.Response(status=200)


async def delete_transcript(request: web.Request, sid) -> web.Response:
    """delete_transcript

    Delete a specific Transcript.

    :param sid: A 34 character string that uniquely identifies this Transcript.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_transcript(request: web.Request, sid) -> web.Response:
    """fetch_transcript

    Fetch a specific Transcript.

    :param sid: A 34 character string that uniquely identifies this Transcript.
    :type sid: str

    """
    return web.Response(status=200)


async def list_transcript(request: web.Request, service_sid=None, before_start_time=None, after_start_time=None, before_date_created=None, after_date_created=None, status=None, language_code=None, source_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_transcript

    Retrieve a list of Transcripts for a given service.

    :param service_sid: The unique SID identifier of the Service.
    :type service_sid: str
    :param before_start_time: Filter by before StartTime.
    :type before_start_time: str
    :param after_start_time: Filter by after StartTime.
    :type after_start_time: str
    :param before_date_created: Filter by before DateCreated.
    :type before_date_created: str
    :param after_date_created: Filter by after DateCreated.
    :type after_date_created: str
    :param status: Filter by status.
    :type status: str
    :param language_code: Filter by Language Code.
    :type language_code: str
    :param source_sid: Filter by SourceSid.
    :type source_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
