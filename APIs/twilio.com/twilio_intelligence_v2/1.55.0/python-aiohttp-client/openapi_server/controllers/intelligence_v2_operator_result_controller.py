from typing import List, Dict
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript_operator_result import IntelligenceV2TranscriptOperatorResult
from openapi_server.models.list_operator_result_response import ListOperatorResultResponse
from openapi_server import util


async def fetch_operator_result(request: web.Request, transcript_sid, operator_sid, redacted=None) -> web.Response:
    """fetch_operator_result

    Fetch a specific Operator Result for the given Transcript.

    :param transcript_sid: A 34 character string that uniquely identifies this Transcript.
    :type transcript_sid: str
    :param operator_sid: A 34 character string that identifies this Language Understanding operator sid.
    :type operator_sid: str
    :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
    :type redacted: bool

    """
    return web.Response(status=200)


async def list_operator_result(request: web.Request, transcript_sid, redacted=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_operator_result

    Retrieve a list of Operator Results for the given Transcript.

    :param transcript_sid: A 34 character string that uniquely identifies this Transcript.
    :type transcript_sid: str
    :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
    :type redacted: bool
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
