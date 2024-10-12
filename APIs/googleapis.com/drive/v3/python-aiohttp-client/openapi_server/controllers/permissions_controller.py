from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission import Permission
from openapi_server.models.permission_list import PermissionList
from openapi_server import util


async def drive_permissions_create(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, email_message=None, enforce_single_parent=None, move_to_new_owners_root=None, send_notification_email=None, supports_all_drives=None, supports_team_drives=None, transfer_ownership=None, use_domain_admin_access=None, body=None) -> web.Response:
    """drive_permissions_create

    Creates a permission for a file or shared drive. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

    :param file_id: The ID of the file or shared drive.
    :type file_id: str
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
    :param email_message: A plain text custom message to include in the notification email.
    :type email_message: str
    :param enforce_single_parent: Deprecated: See &#x60;moveToNewOwnersRoot&#x60; for details.
    :type enforce_single_parent: bool
    :param move_to_new_owners_root: This parameter will only take effect if the item is not in a shared drive and the request is attempting to transfer the ownership of the item. If set to &#x60;true&#x60;, the item will be moved to the new owner&#39;s My Drive root folder and all prior parents removed. If set to &#x60;false&#x60;, parents are not changed.
    :type move_to_new_owners_root: bool
    :param send_notification_email: Whether to send a notification email when sharing to users or groups. This defaults to true for users and groups, and is not allowed for other requests. It must not be disabled for ownership transfers.
    :type send_notification_email: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param transfer_ownership: Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.
    :type transfer_ownership: bool
    :param use_domain_admin_access: Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    :type use_domain_admin_access: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Permission.from_dict(body)
    return web.Response(status=200)


async def drive_permissions_delete(request: web.Request, file_id, permission_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, supports_all_drives=None, supports_team_drives=None, use_domain_admin_access=None) -> web.Response:
    """drive_permissions_delete

    Deletes a permission. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

    :param file_id: The ID of the file or shared drive.
    :type file_id: str
    :param permission_id: The ID of the permission.
    :type permission_id: str
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
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param use_domain_admin_access: Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    :type use_domain_admin_access: bool

    """
    return web.Response(status=200)


async def drive_permissions_get(request: web.Request, file_id, permission_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, supports_all_drives=None, supports_team_drives=None, use_domain_admin_access=None) -> web.Response:
    """drive_permissions_get

    Gets a permission by ID.

    :param file_id: The ID of the file.
    :type file_id: str
    :param permission_id: The ID of the permission.
    :type permission_id: str
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
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param use_domain_admin_access: Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    :type use_domain_admin_access: bool

    """
    return web.Response(status=200)


async def drive_permissions_list(request: web.Request, file_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, include_permissions_for_view=None, page_size=None, page_token=None, supports_all_drives=None, supports_team_drives=None, use_domain_admin_access=None) -> web.Response:
    """drive_permissions_list

    Lists a file&#39;s or shared drive&#39;s permissions.

    :param file_id: The ID of the file or shared drive.
    :type file_id: str
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
    :param include_permissions_for_view: Specifies which additional view&#39;s permissions to include in the response. Only &#39;published&#39; is supported.
    :type include_permissions_for_view: str
    :param page_size: The maximum number of permissions to return per page. When not set for files in a shared drive, at most 100 results will be returned. When not set for files that are not in a shared drive, the entire list will be returned.
    :type page_size: int
    :param page_token: The token for continuing a previous list request on the next page. This should be set to the value of &#39;nextPageToken&#39; from the previous response.
    :type page_token: str
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param use_domain_admin_access: Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    :type use_domain_admin_access: bool

    """
    return web.Response(status=200)


async def drive_permissions_update(request: web.Request, file_id, permission_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, remove_expiration=None, supports_all_drives=None, supports_team_drives=None, transfer_ownership=None, use_domain_admin_access=None, body=None) -> web.Response:
    """drive_permissions_update

    Updates a permission with patch semantics. **Warning:** Concurrent permissions operations on the same file are not supported; only the last update is applied.

    :param file_id: The ID of the file or shared drive.
    :type file_id: str
    :param permission_id: The ID of the permission.
    :type permission_id: str
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
    :param remove_expiration: Whether to remove the expiration date.
    :type remove_expiration: bool
    :param supports_all_drives: Whether the requesting application supports both My Drives and shared drives.
    :type supports_all_drives: bool
    :param supports_team_drives: Deprecated: Use &#x60;supportsAllDrives&#x60; instead.
    :type supports_team_drives: bool
    :param transfer_ownership: Whether to transfer ownership to the specified user and downgrade the current owner to a writer. This parameter is required as an acknowledgement of the side effect.
    :type transfer_ownership: bool
    :param use_domain_admin_access: Issue the request as a domain administrator; if set to true, then the requester will be granted access if the file ID parameter refers to a shared drive and the requester is an administrator of the domain to which the shared drive belongs.
    :type use_domain_admin_access: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Permission.from_dict(body)
    return web.Response(status=200)
