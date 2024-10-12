from typing import List, Dict
from aiohttp import web

from openapi_server.models.change import Change
from openapi_server.models.change_list import ChangeList
from openapi_server.models.channel import Channel
from openapi_server.models.start_page_token import StartPageToken
from openapi_server import util


async def drive_changes_get(request: web.Request, change_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, drive_id=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None) -> web.Response:
    """drive_changes_get

    Deprecated: Use &#x60;changes.getStartPageToken&#x60; and &#x60;changes.list&#x60; to retrieve recent changes.

    :param change_id: The ID of the change.
    :type change_id: str
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
    :param drive_id: The shared drive from which the change will be returned.
    :type drive_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param team_drive_id: Deprecated: Use &#x60;driveId&#x60; instead.
    :type team_drive_id: str

    """
    return web.Response(status=200)


async def drive_changes_get_start_page_token(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, drive_id=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None) -> web.Response:
    """drive_changes_get_start_page_token

    Gets the starting pageToken for listing future changes.

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
    :param drive_id: The ID of the shared drive for which the starting pageToken for listing future changes from that shared drive will be returned.
    :type drive_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param team_drive_id: Deprecated: Use &#x60;driveId&#x60; instead.
    :type team_drive_id: str

    """
    return web.Response(status=200)


async def drive_changes_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, drive_id=None, include_corpus_removals=None, include_deleted=None, include_items_from_all_drives=None, include_labels=None, include_permissions_for_view=None, include_subscribed=None, include_team_drive_items=None, max_results=None, page_token=None, spaces=None, start_change_id=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None) -> web.Response:
    """drive_changes_list

    Lists the changes for a user or shared drive.

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
    :param drive_id: The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.
    :type drive_id: str
    :param include_corpus_removals: Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.
    :type include_corpus_removals: bool
    :param include_deleted: Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.
    :type include_deleted: bool
    :param include_items_from_all_drives: Whether both My Drive and shared drive items should be included in results.
    :type include_items_from_all_drives: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param include_subscribed: Whether to include changes outside the My Drive hierarchy in the result. When set to false, changes to files such as those in the Application Data folder or shared files which have not been added to My Drive will be omitted from the result.
    :type include_subscribed: bool
    :param include_team_drive_items: Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead.
    :type include_team_drive_items: bool
    :param max_results: Maximum number of changes to return.
    :type max_results: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from the previous response or to the response from the getStartPageToken method.
    :type page_token: str
    :param spaces: A comma-separated list of spaces to query. Supported values are &#x60;drive&#x60;, &#x60;appDataFolder&#x60; and &#x60;photos&#x60;.
    :type spaces: str
    :param start_change_id: Deprecated: Use &#x60;pageToken&#x60; instead.
    :type start_change_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param team_drive_id: Deprecated: Use &#x60;driveId&#x60; instead.
    :type team_drive_id: str

    """
    return web.Response(status=200)


async def drive_changes_watch(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, drive_id=None, include_corpus_removals=None, include_deleted=None, include_items_from_all_drives=None, include_labels=None, include_permissions_for_view=None, include_subscribed=None, include_team_drive_items=None, max_results=None, page_token=None, spaces=None, start_change_id=None, supports_all_drives=None, supports_team_drives=None, team_drive_id=None, body=None) -> web.Response:
    """drive_changes_watch

    Subscribe to changes for a user.

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
    :param drive_id: The shared drive from which changes will be returned. If specified the change IDs will be reflective of the shared drive; use the combined drive ID and change ID as an identifier.
    :type drive_id: str
    :param include_corpus_removals: Whether changes should include the file resource if the file is still accessible by the user at the time of the request, even when a file was removed from the list of changes and there will be no further change entries for this file.
    :type include_corpus_removals: bool
    :param include_deleted: Whether to include changes indicating that items have been removed from the list of changes, for example by deletion or loss of access.
    :type include_deleted: bool
    :param include_items_from_all_drives: Whether both My Drive and shared drive items should be included in results.
    :type include_items_from_all_drives: bool
    :param include_labels: A comma-separated list of IDs of labels to include in the &#x60;labelInfo&#x60; part of the response.
    :type include_labels: str
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#x60;published&#x60; is supported.
    :type include_permissions_for_view: str
    :param include_subscribed: Whether to include changes outside the My Drive hierarchy in the result. When set to false, changes to files such as those in the Application Data folder or shared files which have not been added to My Drive will be omitted from the result.
    :type include_subscribed: bool
    :param include_team_drive_items: Deprecated: Use &#x60;includeItemsFromAllDrives&#x60; instead.
    :type include_team_drive_items: bool
    :param max_results: Maximum number of changes to return.
    :type max_results: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#x60;nextPageToken&#x60; from the previous response or to the response from the getStartPageToken method.
    :type page_token: str
    :param spaces: A comma-separated list of spaces to query. Supported values are &#x60;drive&#x60;, &#x60;appDataFolder&#x60; and &#x60;photos&#x60;.
    :type spaces: str
    :param start_change_id: Deprecated: Use &#x60;pageToken&#x60; instead.
    :type start_change_id: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param team_drive_id: Deprecated: Use &#x60;driveId&#x60; instead.
    :type team_drive_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
