from typing import List, Dict
from aiohttp import web

from openapi_server.models.insights_v1_call_summary import InsightsV1CallSummary
from openapi_server.models.summary_enum_processing_state import SummaryEnumProcessingState
from openapi_server import util


async def fetch_summary(request: web.Request, call_sid, processing_state=None) -> web.Response:
    """fetch_summary

    Get a specific Call Summary.

    :param call_sid: The unique SID identifier of the Call.
    :type call_sid: str
    :param processing_state: The Processing State of this Call Summary. One of &#x60;complete&#x60;, &#x60;partial&#x60; or &#x60;all&#x60;.
    :type processing_state: str

    """
    return web.Response(status=200)
