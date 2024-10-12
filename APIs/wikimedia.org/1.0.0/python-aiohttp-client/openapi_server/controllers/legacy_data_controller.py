from typing import List, Dict
from aiohttp import web

from openapi_server.models.pagecounts_project import PagecountsProject
from openapi_server.models.problem import Problem
from openapi_server import util


async def metrics_legacy_pagecounts_aggregate_project_access_site_granularity_start_end_get(request: web.Request, project, access_site, granularity, start, end) -> web.Response:
    """metrics_legacy_pagecounts_aggregate_project_access_site_granularity_start_end_get

    Given a project and a date range, returns a timeseries of pagecounts. You can filter by access site (mobile or desktop) and you can choose between monthly, daily and hourly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. 
    :type project: str
    :param access_site: If you want to filter by access site, use one of desktop-site or mobile-site. If you are interested in pagecounts regardless of access site use all-sites.
    :type access_site: str
    :param granularity: The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily and monthly. 
    :type granularity: str
    :param start: The timestamp of the first hour/day/month to include, in YYYYMMDDHH format.
    :type start: str
    :param end: The timestamp of the last hour/day/month to include, in YYYYMMDDHH format. In hourly and daily granularities this value is inclusive, in the monthly granularity this value is exclusive. 
    :type end: str

    """
    return web.Response(status=200)
