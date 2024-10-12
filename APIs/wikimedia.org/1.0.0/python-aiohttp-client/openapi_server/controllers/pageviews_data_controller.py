from typing import List, Dict
from aiohttp import web

from openapi_server.models.by_country import ByCountry
from openapi_server.models.pageview_article import PageviewArticle
from openapi_server.models.pageview_project import PageviewProject
from openapi_server.models.pageview_tops import PageviewTops
from openapi_server.models.problem import Problem
from openapi_server import util


async def metrics_pageviews_aggregate_project_access_agent_granularity_start_end_get(request: web.Request, project, access, agent, granularity, start, end) -> web.Response:
    """Get pageview counts for a project.

    Given a date range, returns a timeseries of pageview counts. You can filter by project, access method and/or agent type. You can choose between daily and hourly granularity as well.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. If you are interested in all pageviews regardless of project, use all-projects. 
    :type project: str
    :param access: If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
    :type access: str
    :param agent: If you want to filter by agent type, use one of user or spider. If you are interested in pageviews regardless of agent type, use all-agents. 
    :type agent: str
    :param granularity: The time unit for the response data. As of today, the supported granularities for this endpoint are hourly, daily, and monthly. 
    :type granularity: str
    :param start: The timestamp of the first hour/day/month to include, in YYYYMMDDHH format
    :type start: str
    :param end: The timestamp of the last hour/day/month to include, in YYYYMMDDHH format
    :type end: str

    """
    return web.Response(status=200)


async def metrics_pageviews_per_article_project_access_agent_article_granularity_start_end_get(request: web.Request, project, access, agent, article, granularity, start, end) -> web.Response:
    """Get pageview counts for a page.

    Given a Mediawiki article and a date range, returns a daily timeseries of its pageview counts. You can also filter by access method and/or agent type.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. 
    :type project: str
    :param access: If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
    :type access: str
    :param agent: If you want to filter by agent type, use one of user, bot or spider. If you are interested in pageviews regardless of agent type, use all-agents. 
    :type agent: str
    :param article: &#39;The title of any article in the specified project. Any spaces should be replaced with underscores. It also should be URI-encoded, so that non-URI-safe characters like %, / or ? are accepted. Example: Are_You_the_One%3F&#39;. 
    :type article: str
    :param granularity: The time unit for the response data. As of today, the only supported granularity for this endpoint is daily and monthly. 
    :type granularity: str
    :param start: The date of the first day to include, in YYYYMMDD or YYYYMMDDHH format
    :type start: str
    :param end: The date of the last day to include, in YYYYMMDD or YYYYMMDDHH format
    :type end: str

    """
    return web.Response(status=200)


async def metrics_pageviews_top_by_country_project_access_year_month_get(request: web.Request, project, access, year, month) -> web.Response:
    """Get pageviews by country and access method.

    Lists the pageviews to this project, split by country of origin for a given month. Because of privacy reasons, pageviews are given in a bucketed format, and countries with less than 100 views do not get reported. Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. 
    :type project: str
    :param access: If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
    :type access: str
    :param year: The year of the date for which to retrieve top countries, in YYYY format.
    :type year: str
    :param month: The month of the date for which to retrieve top countries, in MM format. 
    :type month: str

    """
    return web.Response(status=200)


async def metrics_pageviews_top_project_access_year_month_day_get(request: web.Request, project, access, year, month, day) -> web.Response:
    """Get the most viewed articles for a project.

    Lists the 1000 most viewed articles for a given project and timespan (month or day). You can filter by access method.  - Stability: [stable](https://www.mediawiki.org/wiki/API_versioning#Stable) - Rate limit: 100 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: If you want to filter by project, use the domain of any Wikimedia project, for example &#39;en.wikipedia.org&#39;, &#39;www.mediawiki.org&#39; or &#39;commons.wikimedia.org&#39;. 
    :type project: str
    :param access: If you want to filter by access method, use one of desktop, mobile-app or mobile-web. If you are interested in pageviews regardless of access method, use all-access. 
    :type access: str
    :param year: The year of the date for which to retrieve top articles, in YYYY format.
    :type year: str
    :param month: The month of the date for which to retrieve top articles, in MM format. If you want to get the top articles of a whole month, the day parameter should be all-days. 
    :type month: str
    :param day: The day of the date for which to retrieve top articles, in DD format.
    :type day: str

    """
    return web.Response(status=200)
