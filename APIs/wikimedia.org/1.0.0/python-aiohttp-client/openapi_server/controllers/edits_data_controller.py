from typing import List, Dict
from aiohttp import web

from openapi_server.models.edits import Edits
from openapi_server.models.edits_per_page import EditsPerPage
from openapi_server.models.problem import Problem
from openapi_server import util


async def metrics_edits_aggregate_project_editor_type_page_type_granularity_start_end_get(request: web.Request, project, editor_type, page_type, granularity, start, end) -> web.Response:
    """Get edits counts for a project.

    Given a Mediawiki project and a date range, returns a timeseries of edits counts. You can filter by editors-type (all-editor-types, anonymous, bot, registered) and page-type (all-page-types, content or non-content). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. If you&#39;re interested in the aggregation of all projects, use all-projects. 
    :type project: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param page_type: If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    :type page_type: str
    :param granularity: The time unit for the response data. As of today, supported values are daily and monthly. 
    :type granularity: str
    :param start: The date of the first day to include, in YYYYMMDD format
    :type start: str
    :param end: The date of the last day to include, in YYYYMMDD format
    :type end: str

    """
    return web.Response(status=200)


async def metrics_edits_per_page_project_page_title_editor_type_granularity_start_end_get(request: web.Request, project, page_title, editor_type, granularity, start, end) -> web.Response:
    """Get edit counts for a page in a project.

    Given a Mediawiki project, a page-title prefixed with its canonical namespace (for instance &#39;User:Jimbo_Wales&#39;) and a date range, returns a timeseries of edit counts. You can filter by editors-type (all-editor-types, anonymous, group-bot, name-bot, user). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    :type project: str
    :param page_title: The page-title to request edits for. It should be prefixed with canonical namespace. Spaces will be converted to underscores. 
    :type page_title: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param granularity: Time unit for the response data. As of today, supported values are daily and monthly 
    :type granularity: str
    :param start: The date of the first day to include, in YYYYMMDD format
    :type start: str
    :param end: The date of the last day to include, in YYYYMMDD format
    :type end: str

    """
    return web.Response(status=200)
