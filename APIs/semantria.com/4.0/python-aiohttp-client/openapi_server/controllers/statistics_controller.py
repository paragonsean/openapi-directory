from typing import List, Dict
from aiohttp import web

from openapi_server.models.statistic import Statistic
from openapi_server import util


async def get_statistic(request: web.Request, content_type, config_id=None, interval=None) -> web.Response:
    """Retrieve usage statistics

    This method retrieves overall and per configuration usage statistics for specific timeframe. Statistics ordered per available configurations. Available interval values are current &lt;b&gt;hour&lt;/b&gt;, &lt;b&gt;day&lt;/b&gt;, &lt;b&gt;week&lt;/b&gt;, &lt;b&gt;month&lt;/b&gt; and &lt;b&gt;year&lt;/b&gt;.

    :param content_type: 
    :type content_type: str
    :param config_id: Configuration identifier for usage statistics retrieving.
    :type config_id: str
    :param interval: Hour, Day, Week, Month, Year values are supported.
    :type interval: str

    """
    return web.Response(status=200)
