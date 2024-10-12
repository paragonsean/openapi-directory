from typing import List, Dict
from aiohttp import web

from openapi_server.models.editors import Editors
from openapi_server.models.problem import Problem
from openapi_server.models.top_editors_by_abs_bytes_diff import TopEditorsByAbsBytesDiff
from openapi_server.models.top_editors_by_edits import TopEditorsByEdits
from openapi_server.models.top_editors_by_net_bytes_diff import TopEditorsByNetBytesDiff
from openapi_server import util


async def metrics_editors_aggregate_project_editor_type_page_type_activity_level_granularity_start_end_get(request: web.Request, project, editor_type, page_type, activity_level, granularity, start, end) -> web.Response:
    """Get editors counts for a project.

    Given a Mediawiki project and a date range, returns a timeseries of its editors counts. You can filter by editory-type (all-editor-types, anonymous, group-bot, name-bot, user), page-type (all-page-types, content or non-content) or activity-level (1..4-edits, 5..24-edits, 25..99-edits or 100..-edits). You can choose between daily and monthly granularity as well.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off.  For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    :type project: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param page_type: If you want to filter by page-type, use one of content (edits made in content namespaces) or non-content (edits made in non-content namespaces). If you are interested in editors regardless of their page-type, use all-page-types. 
    :type page_type: str
    :param activity_level: If you want to filter by activity-level, use one of 1..4-edits, 5..24-edits, 25..99-edits or 100..-edits. If you are interested in editors regardless of their activity-level, use all-activity-levels. 
    :type activity_level: str
    :param granularity: The time unit for the response data. As of today, supported values are daily and monthly. 
    :type granularity: str
    :param start: The date of the first day to include, in YYYYMMDD format
    :type start: str
    :param end: The date of the last day to include, in YYYYMMDD format
    :type end: str

    """
    return web.Response(status=200)


async def metrics_editors_top_by_absolute_bytes_difference_project_editor_type_page_type_year_month_day_get(request: web.Request, project, editor_type, page_type, year, month, day) -> web.Response:
    """Get top 100 editors by absolute bytes-difference.

    Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by absolute bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    :type project: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param page_type: If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    :type page_type: str
    :param year: The year of the date for which to retrieve top editors, in YYYY format.
    :type year: str
    :param month: The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    :type month: str
    :param day: The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    :type day: str

    """
    return web.Response(status=200)


async def metrics_editors_top_by_edits_project_editor_type_page_type_year_month_day_get(request: web.Request, project, editor_type, page_type, year, month, day) -> web.Response:
    """Get top 100 editors by edits count.

    Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by edits count. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or null if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    :type project: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param page_type: If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    :type page_type: str
    :param year: The year of the date for which to retrieve top editors, in YYYY format.
    :type year: str
    :param month: The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    :type month: str
    :param day: The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    :type day: str

    """
    return web.Response(status=200)


async def metrics_editors_top_by_net_bytes_difference_project_editor_type_page_type_year_month_day_get(request: web.Request, project, editor_type, page_type, year, month, day) -> web.Response:
    """Get top 100 editors by net bytes-difference.

    Given a Mediawiki project and a date (day or month), returns a timeseries of the top 100 editors by net bytes-difference. You can filter by editor-type (all-editor-types, anonymous, group-bot, name-bot, user) or page-type (all-page-types, content or non-content). The user_text returned is either the mediawiki user_text if the user is registered, or \&quot;Anonymous Editor\&quot; if user is anonymous.  - Stability: [experimental](https://www.mediawiki.org/wiki/API_versioning#Experimental) - Rate limit: 25 req/s - License: Data accessible via this endpoint is available under the   [CC0 1.0 license](https://creativecommons.org/publicdomain/zero/1.0/). 

    :param project: The name of any Wikimedia project formatted like {language code}.{project name}, for example en.wikipedia. You may pass en.wikipedia.org and the .org will be stripped off. For projects like commons without language codes, use commons.wikimedia. For projects like www.mediawiki.org, you can use that full string, or just use mediawiki or mediawiki.org. 
    :type project: str
    :param editor_type: If you want to filter by editor-type, use one of anonymous, group-bot (registered accounts belonging to the bot group), name-bot (registered accounts not belonging to the bot group but having bot-like names) or user (registered account not in bot group nor having bot-like name). If you are interested in edits regardless of their editor-type, use all-editor-types. 
    :type editor_type: str
    :param page_type: If you want to filter by page-type, use one of content (edits on pages in content namespaces) or non-content (edits on pages in non-content namespaces). If you are interested in edits regardless of their page-type, use all-page-types. 
    :type page_type: str
    :param year: The year of the date for which to retrieve top editors, in YYYY format.
    :type year: str
    :param month: The month of the date for which to retrieve top editors, in MM format. If you want to get the top editors of a whole month, the day parameter should be all-days.
    :type month: str
    :param day: The day of the date for which to retrieve top editors, in DD format, or all-days for a monthly value.
    :type day: str

    """
    return web.Response(status=200)
