from typing import List, Dict
from aiohttp import web

from openapi_server.models.call_report import CallReport
from openapi_server.models.reputation import Reputation
from openapi_server import util


async def reputation_report(request: web.Request, call_report) -> web.Response:
    """Report: report spam calls received to better tune our algorithms based upon spam calls you receive

    This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

    :param call_report: [FromBody] Call Report              PhoneNumber,               Caller name(optional),               Call category(optional),               Comment or tags(free text) (optional),               Unwanted call  - yes/no(optional),
    :type call_report: dict | bytes

    """
    call_report = CallReport.from_dict(call_report)
    return web.Response(status=200)


async def reputation_reputation(request: web.Request, phone_number) -> web.Response:
    """Reputation:  Premium service which returns a reputation informaiton of a phone number via API.

    This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

    :param phone_number: phone number to search
    :type phone_number: str

    """
    return web.Response(status=200)
