from typing import List, Dict
from aiohttp import web

from openapi_server.models.monitor_dep_graph_request import MonitorDepGraphRequest
from openapi_server import util


async def monitor_dep_graph(request: web.Request, org=None, body=None) -> web.Response:
    """Monitor Dep Graph

    Use this endpoint to monitor a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

    :param org: The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above.
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = MonitorDepGraphRequest.from_dict(body)
    return web.Response(status=200)
