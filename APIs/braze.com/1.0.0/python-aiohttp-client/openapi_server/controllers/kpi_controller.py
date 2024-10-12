from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def daily_active_users_by_date_0(request: web.Request, length=None, ending_at=None, app_id=None) -> web.Response:
    """Daily Active Users by Date

    This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;dau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

    :param length: (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    :type length: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    :type app_id: str

    """
    return web.Response(status=200)


async def daily_new_users_by_date_0(request: web.Request, length=None, ending_at=None, app_id=None) -> web.Response:
    """Daily New Users by Date

    This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;new_users\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

    :param length: (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    :type length: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    :type app_id: str

    """
    return web.Response(status=200)


async def kp_is_for_daily_app_uninstalls_by_date_0(request: web.Request, length=None, ending_at=None, app_id=None) -> web.Response:
    """KPIs for Daily App Uninstalls by Date

    This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;uninstalls\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

    :param length: (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    :type length: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    :type app_id: str

    """
    return web.Response(status=200)


async def monthly_active_users_for_last30_days_0(request: web.Request, length=None, ending_at=None, app_id=None) -> web.Response:
    """Monthly Active Users for Last 30 Days

    This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;mau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

    :param length: (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    :type length: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    :type app_id: str

    """
    return web.Response(status=200)
