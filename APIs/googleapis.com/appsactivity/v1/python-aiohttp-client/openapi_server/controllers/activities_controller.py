from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_activities_response import ListActivitiesResponse
from openapi_server import util


async def appsactivity_activities_list(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, drive_ancestor_id=None, drive_file_id=None, grouping_strategy=None, page_size=None, page_token=None, source=None, user_id=None) -> web.Response:
    """appsactivity_activities_list

    Returns a list of activities visible to the current logged in user. Visible activities are determined by the visibility settings of the object that was acted on, e.g. Drive files a user can see. An activity is a record of past events. Multiple events may be merged if they are similar. A request is scoped to activities from a given Google service using the source parameter.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param drive_ancestor_id: Identifies the Drive folder containing the items for which to return activities.
    :type drive_ancestor_id: str
    :param drive_file_id: Identifies the Drive item to return activities for.
    :type drive_file_id: str
    :param grouping_strategy: Indicates the strategy to use when grouping singleEvents items in the associated combinedEvent object.
    :type grouping_strategy: str
    :param page_size: The maximum number of events to return on a page. The response includes a continuation token if there are more events.
    :type page_size: int
    :param page_token: A token to retrieve a specific page of results.
    :type page_token: str
    :param source: The Google service from which to return activities. Possible values of source are:  - drive.google.com
    :type source: str
    :param user_id: The ID used for ACL checks (does not filter the resulting event list by the assigned value). Use the special value me to indicate the currently authenticated user.
    :type user_id: str

    """
    return web.Response(status=200)
