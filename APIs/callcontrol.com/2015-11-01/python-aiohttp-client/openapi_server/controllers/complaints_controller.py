from typing import List, Dict
from aiohttp import web

from openapi_server.models.complaints import Complaints
from openapi_server import util


async def complaints_complaints(request: web.Request, phone_number) -> web.Response:
    """Complaints: Free service (with registration), providing community and government complaint lookup by phone number for up to 2,000 queries per month.  Details include number complaint rates from (FTC, FCC, IRS, Indiana Attorney  General) and key entity tag extractions from complaints.

    This is the main funciton to get data out of the call control reporting system&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

    :param phone_number: phone number to search
    :type phone_number: str

    """
    return web.Response(status=200)
