from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_entity import GroupEntity
from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server.models.permission_entity import PermissionEntity
from openapi_server.models.user_entity import UserEntity
from openapi_server import util


async def delete_groups_group_id_memberships_user_id(request: web.Request, group_id, user_id) -> web.Response:
    """Delete Group User

    Delete Group User

    :param group_id: Group ID from which to remove user.
    :type group_id: int
    :param user_id: User ID to remove from group.
    :type user_id: int

    """
    return web.Response(status=200)


async def delete_groups_id(request: web.Request, id) -> web.Response:
    """Delete Group

    Delete Group

    :param id: Group ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_groups(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None, ids=None) -> web.Response:
    """List Groups

    List Groups

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[name]&#x3D;desc&#x60;). Valid fields are &#x60;name&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;name&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;name&#x60;.
    :type filter_prefix: dict | bytes
    :param ids: Comma-separated list of group ids to include in results.
    :type ids: str

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def get_groups_group_id_permissions(request: web.Request, group_id, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None, path=None, user_id=None, include_groups=None) -> web.Response:
    """List Permissions

    List Permissions

    :param group_id: DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60;
    :type group_id: str
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;.
    :type filter: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;.
    :type filter_prefix: dict | bytes
    :param path: DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead.
    :type path: str
    :param user_id: DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60;
    :type user_id: str
    :param include_groups: If searching by user or group, also include user&#39;s permissions that are inherited from its groups?
    :type include_groups: bool

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def get_groups_group_id_users(request: web.Request, group_id, user_id=None, cursor=None, per_page=None) -> web.Response:
    """List Group Users

    List Group Users

    :param group_id: Group ID.  If provided, will return group_users of this group.
    :type group_id: int
    :param user_id: User ID.  If provided, will return group_users of this user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_groups_id(request: web.Request, id) -> web.Response:
    """Show Group

    Show Group

    :param id: Group ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_groups_group_id_memberships_user_id(request: web.Request, group_id, user_id, admin=None) -> web.Response:
    """Update Group User

    Update Group User

    :param group_id: Group ID to add user to.
    :type group_id: int
    :param user_id: User ID to add to group.
    :type user_id: int
    :param admin: Is the user a group administrator?
    :type admin: bool

    """
    return web.Response(status=200)


async def patch_groups_id(request: web.Request, id, admin_ids=None, name=None, notes=None, user_ids=None) -> web.Response:
    """Update Group

    Update Group

    :param id: Group ID.
    :type id: int
    :param admin_ids: A list of group admin user ids. If sent as a string, should be comma-delimited.
    :type admin_ids: str
    :param name: Group name.
    :type name: str
    :param notes: Group notes.
    :type notes: str
    :param user_ids: A list of user ids. If sent as a string, should be comma-delimited.
    :type user_ids: str

    """
    return web.Response(status=200)


async def post_groups(request: web.Request, admin_ids=None, name=None, notes=None, user_ids=None) -> web.Response:
    """Create Group

    Create Group

    :param admin_ids: A list of group admin user ids. If sent as a string, should be comma-delimited.
    :type admin_ids: str
    :param name: Group name.
    :type name: str
    :param notes: Group notes.
    :type notes: str
    :param user_ids: A list of user ids. If sent as a string, should be comma-delimited.
    :type user_ids: str

    """
    return web.Response(status=200)


async def post_groups_group_id_users(request: web.Request, group_id, allowed_ips=None, announcements_read=None, attachments_permission=None, authenticate_until=None, authentication_method=None, avatar_delete=None, avatar_file=None, billing_permission=None, bypass_inactive_disable=None, bypass_site_allowed_ips=None, change_password=None, change_password_confirmation=None, company=None, dav_permission=None, disabled=None, email=None, ftp_permission=None, grant_permission=None, group_ids=None, header_text=None, imported_password_hash=None, language=None, name=None, notes=None, notification_daily_send_time=None, office_integration_enabled=None, password=None, password_confirmation=None, password_validity_days=None, receive_admin_alerts=None, require_2fa=None, require_password_change=None, restapi_permission=None, self_managed=None, sftp_permission=None, site_admin=None, skip_welcome_screen=None, ssl_required=None, sso_strategy_id=None, subscribe_to_newsletter=None, time_zone=None, user_root=None, username=None) -> web.Response:
    """Create User

    Create User

    :param group_id: Group ID to associate this user with.
    :type group_id: int
    :param allowed_ips: A list of allowed IPs if applicable.  Newline delimited
    :type allowed_ips: str
    :param announcements_read: Signifies that the user has read all the announcements in the UI.
    :type announcements_read: bool
    :param attachments_permission: DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead.
    :type attachments_permission: bool
    :param authenticate_until: Scheduled Date/Time at which user will be deactivated
    :type authenticate_until: str
    :param authentication_method: How is this user authenticated?
    :type authentication_method: str
    :param avatar_delete: If true, the avatar will be deleted.
    :type avatar_delete: bool
    :param avatar_file: An image file for your user avatar.
    :type avatar_file: str
    :param billing_permission: Allow this user to perform operations on the account, payments, and invoices?
    :type billing_permission: bool
    :param bypass_inactive_disable: Exempt this user from being disabled based on inactivity?
    :type bypass_inactive_disable: bool
    :param bypass_site_allowed_ips: Allow this user to skip site-wide IP blacklists?
    :type bypass_site_allowed_ips: bool
    :param change_password: Used for changing a password on an existing user.
    :type change_password: str
    :param change_password_confirmation: Optional, but if provided, we will ensure that it matches the value sent in &#x60;change_password&#x60;.
    :type change_password_confirmation: str
    :param company: User&#39;s company
    :type company: str
    :param dav_permission: Can the user connect with WebDAV?
    :type dav_permission: bool
    :param disabled: Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting.
    :type disabled: bool
    :param email: User&#39;s email.
    :type email: str
    :param ftp_permission: Can the user access with FTP/FTPS?
    :type ftp_permission: bool
    :param grant_permission: Permission to grant on the user root.  Can be blank or &#x60;full&#x60;, &#x60;read&#x60;, &#x60;write&#x60;, &#x60;list&#x60;, &#x60;read+write&#x60;, or &#x60;list+write&#x60;
    :type grant_permission: str
    :param group_ids: A list of group ids to associate this user with.  Comma delimited.
    :type group_ids: str
    :param header_text: Text to display to the user in the header of the UI
    :type header_text: str
    :param imported_password_hash: Pre-calculated hash of the user&#39;s password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256.
    :type imported_password_hash: str
    :param language: Preferred language
    :type language: str
    :param name: User&#39;s full name
    :type name: str
    :param notes: Any internal notes on the user
    :type notes: str
    :param notification_daily_send_time: Hour of the day at which daily notifications should be sent. Can be in range 0 to 23
    :type notification_daily_send_time: int
    :param office_integration_enabled: Enable integration with Office for the web?
    :type office_integration_enabled: bool
    :param password: User password.
    :type password: str
    :param password_confirmation: Optional, but if provided, we will ensure that it matches the value sent in &#x60;password&#x60;.
    :type password_confirmation: str
    :param password_validity_days: Number of days to allow user to use the same password
    :type password_validity_days: int
    :param receive_admin_alerts: Should the user receive admin alerts such a certificate expiration notifications and overages?
    :type receive_admin_alerts: bool
    :param require_2fa: 2FA required setting
    :type require_2fa: str
    :param require_password_change: Is a password change required upon next user login?
    :type require_password_change: bool
    :param restapi_permission: Can this user access the REST API?
    :type restapi_permission: bool
    :param self_managed: Does this user manage it&#39;s own credentials or is it a shared/bot user?
    :type self_managed: bool
    :param sftp_permission: Can the user access with SFTP?
    :type sftp_permission: bool
    :param site_admin: Is the user an administrator for this site?
    :type site_admin: bool
    :param skip_welcome_screen: Skip Welcome page in the UI?
    :type skip_welcome_screen: bool
    :param ssl_required: SSL required setting
    :type ssl_required: str
    :param sso_strategy_id: SSO (Single Sign On) strategy ID for the user, if applicable.
    :type sso_strategy_id: int
    :param subscribe_to_newsletter: Is the user subscribed to the newsletter?
    :type subscribe_to_newsletter: bool
    :param time_zone: User time zone
    :type time_zone: str
    :param user_root: Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface.
    :type user_root: str
    :param username: User&#39;s username
    :type username: str

    """
    authenticate_until = util.deserialize_datetime(authenticate_until)
    return web.Response(status=200)
