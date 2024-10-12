from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sentence_response import ListSentenceResponse
from openapi_server import util


async def list_sentence(request: web.Request, transcript_sid, redacted=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sentence

    Get all Transcript Sentences by TranscriptSid

    :param transcript_sid: The unique SID identifier of the Transcript.
    :type transcript_sid: str
    :param redacted: Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is &#x60;true&#x60; to access redacted sentences.
    :type redacted: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
