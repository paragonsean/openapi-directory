from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_registered_users import NewRegisteredUsers
from openapi_server.models.problem import Problem
from openapi_server import util


async def metrics_registered_users_new_project_granularity_start_end_get(request: web.Request, project, granularity, start, end) -> web.Response:
    """Get newly registered users counts for a project.

    Given a Mediawiki project and a date range, returns a timeseries of its newly registered users counts. You can choose between daily and monthly granularity. The newly registered users value is computed with self-created users only, not auto-login created ones.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all. 
    :type project: str
    :param granularity: The time unit for the response data. As of today, supported values are daily and monthly. 
    :type granularity: str
    :param start: The date of the first day to include, in YYYYMMDD format
    :type start: str
    :param end: The date of the last day to include, in YYYYMMDD format
    :type end: str

    """
    return web.Response(status=200)
