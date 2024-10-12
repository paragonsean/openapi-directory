from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_log import ChangeLog
from openapi_server.models.change_logs_list_response import ChangeLogsListResponse
from openapi_server import util


async def dfareporting_change_logs_get(request: web.Request, profile_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """dfareporting_change_logs_get

    Gets one change log by ID.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param id: Change log ID.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def dfareporting_change_logs_list(request: web.Request, profile_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, action=None, ids=None, max_change_time=None, max_results=None, min_change_time=None, object_ids=None, object_type=None, page_token=None, search_string=None, user_profile_ids=None) -> web.Response:
    """dfareporting_change_logs_list

    Retrieves a list of change logs. This method supports paging.

    :param profile_id: User profile ID associated with this request.
    :type profile_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param action: Select only change logs with the specified action.
    :type action: str
    :param ids: Select only change logs with these IDs.
    :type ids: List[str]
    :param max_change_time: Select only change logs whose change time is before the specified maxChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \&quot;2015-07-18T22:54:00-04:00\&quot;. In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.
    :type max_change_time: str
    :param max_results: Maximum number of results to return.
    :type max_results: int
    :param min_change_time: Select only change logs whose change time is after the specified minChangeTime.The time should be formatted as an RFC3339 date/time string. For example, for 10:54 PM on July 18th, 2015, in the America/New York time zone, the format is \&quot;2015-07-18T22:54:00-04:00\&quot;. In other words, the year, month, day, the letter T, the hour (24-hour clock system), minute, second, and then the time zone offset.
    :type min_change_time: str
    :param object_ids: Select only change logs with these object IDs.
    :type object_ids: List[str]
    :param object_type: Select only change logs with the specified object type.
    :type object_type: str
    :param page_token: Value of the nextPageToken from the previous result page.
    :type page_token: str
    :param search_string: Select only change logs whose object ID, user name, old or new values match the search string.
    :type search_string: str
    :param user_profile_ids: Select only change logs with these user profile IDs.
    :type user_profile_ids: List[str]

    """
    return web.Response(status=200)
