from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem import Problem
from openapi_server.models.unique_devices import UniqueDevices
from openapi_server import util


async def metrics_unique_devices_project_access_site_granularity_start_end_get(request: web.Request, project, access_site, granularity, start, end) -> web.Response:
    """Get unique devices count per project

    Given a project and a date range, returns a timeseries of unique devices counts. You need to specify a project, and can filter by accessed site (mobile or desktop). You can choose between daily and hourly granularity as well.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. 
    :type project: str
    :param access_site: If you want to filter by accessed site, use one of desktop-site or mobile-site. If you are interested in unique devices regardless of accessed site, use or all-sites. 
    :type access_site: str
    :param granularity: The time unit for the response data. As of today, the supported granularities for this endpoint are daily and monthly. 
    :type granularity: str
    :param start: The timestamp of the first day/month to include, in YYYYMMDD format
    :type start: str
    :param end: The timestamp of the last day/month to include, in YYYYMMDD format
    :type end: str

    """
    return web.Response(status=200)
