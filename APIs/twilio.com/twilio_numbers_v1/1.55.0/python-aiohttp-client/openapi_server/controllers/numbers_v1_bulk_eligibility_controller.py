from typing import List, Dict
from aiohttp import web

from openapi_server.models.numbers_v1_bulk_eligibility import NumbersV1BulkEligibility
from openapi_server import util


async def fetch_bulk_eligibility(request: web.Request, request_id) -> web.Response:
    """fetch_bulk_eligibility

    Fetch an eligibility bulk check that you requested to host in Twilio.

    :param request_id: The SID of the bulk eligibility check that you want to know about.
    :type request_id: str

    """
    return web.Response(status=200)
