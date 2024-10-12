from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.usage_network_stream_sources import UsageNetworkStreamSources
from openapi_server.models.usage_network_stream_targets import UsageNetworkStreamTargets
from openapi_server.models.usage_network_transcoders import UsageNetworkTranscoders
from openapi_server import util


async def usage_network_stream_sources_index(request: web.Request, _from=None, to=None) -> web.Response:
    """Fetch network usage for all stream sources

    This operation shows the amount of network usage for all stream sources in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

    :param _from: The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date.
    :type _from: str
    :param to: The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def usage_network_stream_targets_index(request: web.Request, _from=None, to=None) -> web.Response:
    """Fetch network usage for all stream targets

    This operation shows the amount of network usage for all stream targets in the account cumulatively and individually. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

    :param _from: The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date.
    :type _from: str
    :param to: The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day.
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def usage_network_transcoders_index(request: web.Request, _from=None, to=None, transcoder_type=None, billing_mode=None) -> web.Response:
    """Fetch network usage for all transcoders

    This operation shows the amount of network usage (egress) for all transcoders in the account. The default time frame is &lt;em&gt;from&lt;/em&gt; the last billing date &lt;em&gt;to&lt;/em&gt; the end of the current day.

    :param _from: The start of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;from&lt;/em&gt; default is the last billing date.
    :type _from: str
    :param to: The end of the range of time you want to view. Specify &lt;strong&gt;YYYY-MM-DD HH:MM:SS&lt;/strong&gt; where &lt;strong&gt;HH&lt;/strong&gt; is a 24-hour clock in UTC. The &lt;em&gt;to&lt;/em&gt; default is the end of the current day.
    :type to: str
    :param transcoder_type: The type of transcoder. The default is &lt;strong&gt;transcoded&lt;/strong&gt;.
    :type transcoder_type: str
    :param billing_mode: The billing mode for the transcoder. The default is &lt;strong&gt;pay_as_you_go&lt;/strong&gt;.
    :type billing_mode: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
