from typing import List, Dict
from aiohttp import web

from openapi_server.models.floodlight_activity import FloodlightActivity
from openapi_server.models.floodlight_group import FloodlightGroup
from openapi_server.models.list_floodlight_activities_response import ListFloodlightActivitiesResponse
from openapi_server import util


async def displayvideo_floodlight_groups_floodlight_activities_get(request: web.Request, floodlight_group_id, floodlight_activity_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, partner_id=None) -> web.Response:
    """displayvideo_floodlight_groups_floodlight_activities_get

    Gets a Floodlight activity.

    :param floodlight_group_id: Required. The ID of the parent Floodlight group to which the requested Floodlight activity belongs.
    :type floodlight_group_id: str
    :param floodlight_activity_id: Required. The ID of the Floodlight activity to fetch.
    :type floodlight_activity_id: str
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
    :param partner_id: Required. The ID of the partner through which the Floodlight activity is being accessed.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_floodlight_groups_floodlight_activities_list(request: web.Request, floodlight_group_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, order_by=None, page_size=None, page_token=None, partner_id=None) -> web.Response:
    """displayvideo_floodlight_groups_floodlight_activities_list

    Lists Floodlight activities in a Floodlight group.

    :param floodlight_group_id: Required. The ID of the parent Floodlight group to which the requested Floodlight activities belong.
    :type floodlight_group_id: str
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
    :param order_by: Optional. Field by which to sort the list. Acceptable values are: * &#x60;displayName&#x60; (default) * &#x60;floodlightActivityId&#x60; The default sorting order is ascending. To specify descending order for a field, a suffix \&quot;desc\&quot; should be added to the field name. Example: &#x60;displayName desc&#x60;.
    :type order_by: str
    :param page_size: Optional. Requested page size. Must be between &#x60;1&#x60; and &#x60;100&#x60;. If unspecified will default to &#x60;100&#x60;. Returns error code &#x60;INVALID_ARGUMENT&#x60; if an invalid value is specified.
    :type page_size: int
    :param page_token: Optional. A token identifying a page of results the server should return. Typically, this is the value of next_page_token returned from the previous call to &#x60;ListFloodlightActivities&#x60; method. If not specified, the first page of results will be returned.
    :type page_token: str
    :param partner_id: Required. The ID of the partner through which the Floodlight activities are being accessed.
    :type partner_id: str

    """
    return web.Response(status=200)


async def displayvideo_floodlight_groups_get(request: web.Request, floodlight_group_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, partner_id=None) -> web.Response:
    """displayvideo_floodlight_groups_get

    Gets a Floodlight group.

    :param floodlight_group_id: Required. The ID of the Floodlight group to fetch.
    :type floodlight_group_id: str
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
    :param partner_id: Required. The partner context by which the Floodlight group is being accessed.
    :type partner_id: str

    """
    return web.Response(status=200)
