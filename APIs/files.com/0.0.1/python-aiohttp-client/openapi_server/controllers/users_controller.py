from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server.models.permission_entity import PermissionEntity
from openapi_server.models.public_key_entity import PublicKeyEntity
from openapi_server.models.user_cipher_use_entity import UserCipherUseEntity
from openapi_server.models.user_entity import UserEntity
from openapi_server import util


async def delete_users_id(request: web.Request, id) -> web.Response:
    """Delete User

    Delete User

    :param id: User ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_users(request: web.Request, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_prefix=None, filter_lt=None, filter_lteq=None, ids=None, q_username=None, q_email=None, q_notes=None, q_admin=None, q_allowed_ips=None, q_password_validity_days=None, q_ssl_required=None, search=None) -> web.Response:
    """List Users

    List Users

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[authenticate_until]&#x3D;desc&#x60;). Valid fields are &#x60;authenticate_until&#x60;, &#x60;active&#x60;, &#x60;email&#x60;, &#x60;last_desktop_login_at&#x60;, &#x60;last_login_at&#x60;, &#x60;username&#x60;, &#x60;company&#x60;, &#x60;name&#x60;, &#x60;site_admin&#x60;, &#x60;receive_admin_alerts&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60; or &#x60;not_site_admin&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60;, &#x60;company&#x60;, &#x60;site_admin&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60;, &#x60;last_login_at&#x60;, &#x60;authenticate_until&#x60; or &#x60;not_site_admin&#x60;. Valid field combinations are &#x60;[ not_site_admin, username ]&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_prefix: If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60; or &#x60;company&#x60;.
    :type filter_prefix: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;.
    :type filter_lteq: dict | bytes
    :param ids: comma-separated list of User IDs
    :type ids: str
    :param q_username: List users matching username.
    :type q_username: str
    :param q_email: List users matching email.
    :type q_email: str
    :param q_notes: List users matching notes field.
    :type q_notes: str
    :param q_admin: If &#x60;true&#x60;, list only admin users.
    :type q_admin: str
    :param q_allowed_ips: If set, list only users with overridden allowed IP setting.
    :type q_allowed_ips: str
    :param q_password_validity_days: If set, list only users with overridden password validity days setting.
    :type q_password_validity_days: str
    :param q_ssl_required: If set, list only users with overridden SSL required setting.
    :type q_ssl_required: str
    :param search: Searches for partial matches of name, username, or email.
    :type search: str

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_prefix = .from_dict(filter_prefix)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_users_id(request: web.Request, id) -> web.Response:
    """Show User

    Show User

    :param id: User ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_users_user_id_api_keys(request: web.Request, user_id, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None) -> web.Response:
    """List Api Keys

    List Api Keys

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param sort_by: If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;.
    :type sort_by: dict | bytes
    :param filter: If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter: dict | bytes
    :param filter_gt: If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_gt: dict | bytes
    :param filter_gteq: If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_gteq: dict | bytes
    :param filter_lt: If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_lt: dict | bytes
    :param filter_lteq: If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;.
    :type filter_lteq: dict | bytes

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_gt = .from_dict(filter_gt)
    filter_gteq = .from_dict(filter_gteq)
    filter_lt = .from_dict(filter_lt)
    filter_lteq = .from_dict(filter_lteq)
    return web.Response(status=200)


async def get_users_user_id_cipher_uses(request: web.Request, user_id, cursor=None, per_page=None) -> web.Response:
    """List User Cipher Uses

    List User Cipher Uses

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_users_user_id_groups(request: web.Request, user_id, cursor=None, per_page=None, group_id=None) -> web.Response:
    """List Group Users

    List Group Users

    :param user_id: User ID.  If provided, will return group_users of this user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int
    :param group_id: Group ID.  If provided, will return group_users of this group.
    :type group_id: int

    """
    return web.Response(status=200)


async def get_users_user_id_permissions(request: web.Request, user_id, cursor=None, per_page=None, sort_by=None, filter=None, filter_prefix=None, path=None, group_id=None, include_groups=None) -> web.Response:
    """List Permissions

    List Permissions

    :param user_id: DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60;
    :type user_id: str
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
    :param group_id: DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60;
    :type group_id: str
    :param include_groups: If searching by user or group, also include user&#39;s permissions that are inherited from its groups?
    :type include_groups: bool

    """
    sort_by = .from_dict(sort_by)
    filter = .from_dict(filter)
    filter_prefix = .from_dict(filter_prefix)
    return web.Response(status=200)


async def get_users_user_id_public_keys(request: web.Request, user_id, cursor=None, per_page=None) -> web.Response:
    """List Public Keys

    List Public Keys

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def patch_users_id(request: web.Request, id, allowed_ips=None, announcements_read=None, attachments_permission=None, authenticate_until=None, authentication_method=None, avatar_delete=None, avatar_file=None, billing_permission=None, bypass_inactive_disable=None, bypass_site_allowed_ips=None, change_password=None, change_password_confirmation=None, company=None, dav_permission=None, disabled=None, email=None, ftp_permission=None, grant_permission=None, group_id=None, group_ids=None, header_text=None, imported_password_hash=None, language=None, name=None, notes=None, notification_daily_send_time=None, office_integration_enabled=None, password=None, password_confirmation=None, password_validity_days=None, receive_admin_alerts=None, require_2fa=None, require_password_change=None, restapi_permission=None, self_managed=None, sftp_permission=None, site_admin=None, skip_welcome_screen=None, ssl_required=None, sso_strategy_id=None, subscribe_to_newsletter=None, time_zone=None, user_root=None, username=None) -> web.Response:
    """Update User

    Update User

    :param id: User ID.
    :type id: int
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
    :param group_id: Group ID to associate this user with.
    :type group_id: int
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


async def post_users(request: web.Request, allowed_ips=None, announcements_read=None, attachments_permission=None, authenticate_until=None, authentication_method=None, avatar_delete=None, avatar_file=None, billing_permission=None, bypass_inactive_disable=None, bypass_site_allowed_ips=None, change_password=None, change_password_confirmation=None, company=None, dav_permission=None, disabled=None, email=None, ftp_permission=None, grant_permission=None, group_id=None, group_ids=None, header_text=None, imported_password_hash=None, language=None, name=None, notes=None, notification_daily_send_time=None, office_integration_enabled=None, password=None, password_confirmation=None, password_validity_days=None, receive_admin_alerts=None, require_2fa=None, require_password_change=None, restapi_permission=None, self_managed=None, sftp_permission=None, site_admin=None, skip_welcome_screen=None, ssl_required=None, sso_strategy_id=None, subscribe_to_newsletter=None, time_zone=None, user_root=None, username=None) -> web.Response:
    """Create User

    Create User

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
    :param group_id: Group ID to associate this user with.
    :type group_id: int
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


async def post_users_id2fa_reset(request: web.Request, id) -> web.Response:
    """Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

    Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

    :param id: User ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_users_id_resend_welcome_email(request: web.Request, id) -> web.Response:
    """Resend user welcome email

    Resend user welcome email

    :param id: User ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_users_id_unlock(request: web.Request, id) -> web.Response:
    """Unlock user who has been locked out due to failed logins.

    Unlock user who has been locked out due to failed logins.

    :param id: User ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_users_user_id_api_keys(request: web.Request, user_id, description=None, expires_at=None, name=None, path=None, permission_set=None) -> web.Response:
    """Create Api Key

    Create Api Key

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param description: User-supplied description of API key.
    :type description: str
    :param expires_at: API Key expiration date
    :type expires_at: str
    :param name: Internal name for the API Key.  For your use.
    :type name: str
    :param path: Folder path restriction for this api key.
    :type path: str
    :param permission_set: Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    :type permission_set: str

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)


async def post_users_user_id_public_keys(request: web.Request, user_id, public_key, title) -> web.Response:
    """Create Public Key

    Create Public Key

    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int
    :param public_key: Actual contents of SSH key.
    :type public_key: str
    :param title: Internal reference for key.
    :type title: str

    """
    return web.Response(status=200)
