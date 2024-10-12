from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def delete_archived_call(request: web.Request, _date, sid) -> web.Response:
    """delete_archived_call

    Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

    :param _date: The date of the Call in UTC.
    :type _date: str
    :param sid: The Twilio-provided Call SID that uniquely identifies the Call resource to delete
    :type sid: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)
