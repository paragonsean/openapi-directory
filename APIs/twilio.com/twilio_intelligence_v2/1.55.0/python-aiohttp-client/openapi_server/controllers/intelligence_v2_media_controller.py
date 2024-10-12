from typing import List, Dict
from aiohttp import web

from openapi_server.models.intelligence_v2_transcript_media import IntelligenceV2TranscriptMedia
from openapi_server import util


async def fetch_media(request: web.Request, sid, redacted=None) -> web.Response:
    """fetch_media

    Get download URLs for media if possible

    :param sid: The unique SID identifier of the Transcript.
    :type sid: str
    :param redacted: Grant access to PII Redacted/Unredacted Media. If redaction is enabled, the default is &#x60;true&#x60; to access redacted media.
    :type redacted: bool

    """
    return web.Response(status=200)
