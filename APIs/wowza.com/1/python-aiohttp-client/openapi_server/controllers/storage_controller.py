from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.usage_storage_peak_recording import UsageStoragePeakRecording
from openapi_server import util


async def usage_storage_peak_recording_index(request: web.Request, _from=None, to=None) -> web.Response:
    """Fetch peak recording storage

    This operation shows the amount of peak recording storage used for the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

    :param _from: The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date.
    :type _from: str
    :param to: The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
