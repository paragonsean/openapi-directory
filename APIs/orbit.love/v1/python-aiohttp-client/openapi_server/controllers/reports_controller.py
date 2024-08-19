from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def workspace_slug_reports_get(request: web.Request, workspace_slug, start_date=None, end_date=None, relative=None, properties=None, activity_type=None, type=None) -> web.Response:
    """Get a workspace stats

    

    :param workspace_slug: 
    :type workspace_slug: str
    :param start_date: Filter activities after this date. Format: YYYY-MM-DD.
    :type start_date: str
    :param end_date: Filter activities before this date. Format: YYYY-MM-DD.
    :type end_date: str
    :param relative: Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days.
    :type relative: str
    :param properties: 
    :type properties: str
    :param activity_type: 
    :type activity_type: str
    :param type: Deprecated in favor of the activity_type parameter.
    :type type: str

    """
    return web.Response(status=200)
