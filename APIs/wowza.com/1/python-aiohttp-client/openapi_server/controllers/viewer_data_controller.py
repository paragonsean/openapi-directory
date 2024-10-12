from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error410 import Error410
from openapi_server.models.usage_viewer_data_stream_target import UsageViewerDataStreamTarget
from openapi_server import util


async def show_viewer_data_stream_target(request: web.Request, id, _from=None, to=None) -> web.Response:
    """Fetch viewer data for a stream target

    This operation shows viewer data for a specific stream target. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

    :param id: The unique alphanumeric string that identifies the stream target.
    :type id: str
    :param _from: The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date.
    :type _from: str
    :param to: The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
