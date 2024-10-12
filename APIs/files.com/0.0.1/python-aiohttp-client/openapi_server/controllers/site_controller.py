from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server.models.dns_record_entity import DnsRecordEntity
from openapi_server.models.ip_address_entity import IpAddressEntity
from openapi_server.models.site_entity import SiteEntity
from openapi_server.models.status_entity import StatusEntity
from openapi_server.models.usage_snapshot_entity import UsageSnapshotEntity
from openapi_server import util


async def get_site(request: web.Request, ) -> web.Response:
    """Show site settings

    Show site settings


    """
    return web.Response(status=200)


async def get_site_api_keys(request: web.Request, user_id=None, cursor=None, per_page=None, sort_by=None, filter=None, filter_gt=None, filter_gteq=None, filter_lt=None, filter_lteq=None) -> web.Response:
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


async def get_site_dns_records(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """Show site DNS configuration.

    Show site DNS configuration.

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_site_ip_addresses(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List IP Addresses associated with the current site

    List IP Addresses associated with the current site

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_site_usage(request: web.Request, ) -> web.Response:
    """Get the most recent usage snapshot (usage data for billing purposes) for a Site.

    Get the most recent usage snapshot (usage data for billing purposes) for a Site.


    """
    return web.Response(status=200)


async def patch_site(request: web.Request, active_sftp_host_key_id=None, allow_bundle_names=None, allowed_2fa_method_bypass_for_ftp_sftp_dav=None, allowed_2fa_method_sms=None, allowed_2fa_method_totp=None, allowed_2fa_method_u2f=None, allowed_2fa_method_webauthn=None, allowed_2fa_method_yubi=None, allowed_countries=None, allowed_ips=None, ask_about_overwrites=None, bundle_activity_notifications=None, bundle_expiration=None, bundle_password_required=None, bundle_registration_notifications=None, bundle_require_share_recipient=None, bundle_upload_receipt_notifications=None, bundle_watermark_attachment_delete=None, bundle_watermark_attachment_file=None, bundle_watermark_value=None, color2_left=None, color2_link=None, color2_text=None, color2_top=None, color2_top_text=None, custom_namespace=None, days_to_retain_backups=None, default_time_zone=None, desktop_app=None, desktop_app_session_ip_pinning=None, desktop_app_session_lifetime=None, disable_2fa_with_delay=None, disable_files_certificate_generation=None, disable_password_reset=None, disable_users_from_inactivity_period_days=None, disallowed_countries=None, domain=None, domain_hsts_header=None, domain_letsencrypt_chain=None, email=None, folder_permissions_groups_only=None, ftp_enabled=None, icon128_delete=None, icon128_file=None, icon16_delete=None, icon16_file=None, icon32_delete=None, icon32_file=None, icon48_delete=None, icon48_file=None, immutable_files=None, include_password_in_welcome_email=None, language=None, ldap_base_dn=None, ldap_domain=None, ldap_enabled=None, ldap_group_action=None, ldap_group_exclusion=None, ldap_group_inclusion=None, ldap_host=None, ldap_host_2=None, ldap_host_3=None, ldap_password_change=None, ldap_password_change_confirmation=None, ldap_port=None, ldap_secure=None, ldap_type=None, ldap_user_action=None, ldap_user_include_groups=None, ldap_username=None, ldap_username_field=None, login_help_text=None, logo_delete=None, logo_file=None, max_prior_passwords=None, mobile_app=None, mobile_app_session_ip_pinning=None, mobile_app_session_lifetime=None, motd_text=None, motd_use_for_ftp=None, motd_use_for_sftp=None, name=None, non_sso_groups_allowed=None, non_sso_users_allowed=None, office_integration_available=None, office_integration_type=None, opt_out_global=None, password_min_length=None, password_require_letter=None, password_require_mixed=None, password_require_number=None, password_require_special=None, password_require_unbreached=None, password_requirements_apply_to_bundles=None, password_validity_days=None, pin_all_remote_servers_to_site_region=None, reply_to_email=None, require_2fa=None, require_2fa_user_type=None, session_expiry=None, session_expiry_minutes=None, session_pinned_by_ip=None, sftp_enabled=None, sftp_host_key_type=None, sftp_insecure_ciphers=None, sftp_user_root_enabled=None, sharing_enabled=None, show_request_access_link=None, site_footer=None, site_header=None, smtp_address=None, smtp_authentication=None, smtp_from=None, smtp_password=None, smtp_port=None, smtp_username=None, ssl_required=None, subdomain=None, tls_disabled=None, uploads_via_email_authentication=None, use_provided_modified_at=None, user_lockout=None, user_lockout_lock_period=None, user_lockout_tries=None, user_lockout_within=None, user_requests_enabled=None, user_requests_notify_admins=None, welcome_custom_text=None, welcome_email_cc=None, welcome_email_enabled=None, welcome_email_subject=None, welcome_screen=None, windows_mode_ftp=None) -> web.Response:
    """Update site settings.

    Update site settings.

    :param active_sftp_host_key_id: Id of the currently selected custom SFTP Host Key
    :type active_sftp_host_key_id: int
    :param allow_bundle_names: Are manual Bundle names allowed?
    :type allow_bundle_names: bool
    :param allowed_2fa_method_bypass_for_ftp_sftp_dav: Are users allowed to configure their two factor authentication to be bypassed for FTP/SFTP/WebDAV?
    :type allowed_2fa_method_bypass_for_ftp_sftp_dav: bool
    :param allowed_2fa_method_sms: Is SMS two factor authentication allowed?
    :type allowed_2fa_method_sms: bool
    :param allowed_2fa_method_totp: Is TOTP two factor authentication allowed?
    :type allowed_2fa_method_totp: bool
    :param allowed_2fa_method_u2f: Is U2F two factor authentication allowed?
    :type allowed_2fa_method_u2f: bool
    :param allowed_2fa_method_webauthn: Is WebAuthn two factor authentication allowed?
    :type allowed_2fa_method_webauthn: bool
    :param allowed_2fa_method_yubi: Is yubikey two factor authentication allowed?
    :type allowed_2fa_method_yubi: bool
    :param allowed_countries: Comma seperated list of allowed Country codes
    :type allowed_countries: str
    :param allowed_ips: List of allowed IP addresses
    :type allowed_ips: str
    :param ask_about_overwrites: If false, rename conflicting files instead of asking for overwrite confirmation.  Only applies to web interface.
    :type ask_about_overwrites: bool
    :param bundle_activity_notifications: Do Bundle owners receive activity notifications?
    :type bundle_activity_notifications: str
    :param bundle_expiration: Site-wide Bundle expiration in days
    :type bundle_expiration: int
    :param bundle_password_required: Do Bundles require password protection?
    :type bundle_password_required: bool
    :param bundle_registration_notifications: Do Bundle owners receive registration notification?
    :type bundle_registration_notifications: str
    :param bundle_require_share_recipient: Do Bundles require recipients for sharing?
    :type bundle_require_share_recipient: bool
    :param bundle_upload_receipt_notifications: Do Bundle uploaders receive upload confirmation notifications?
    :type bundle_upload_receipt_notifications: str
    :param bundle_watermark_attachment_delete: If true, will delete the file stored in bundle_watermark_attachment
    :type bundle_watermark_attachment_delete: bool
    :param bundle_watermark_attachment_file: 
    :type bundle_watermark_attachment_file: str
    :param bundle_watermark_value: Preview watermark settings applied to all bundle items. Uses the same keys as Behavior.value
    :type bundle_watermark_value: dict | bytes
    :param color2_left: Page link and button color
    :type color2_left: str
    :param color2_link: Top bar link color
    :type color2_link: str
    :param color2_text: Page link and button color
    :type color2_text: str
    :param color2_top: Top bar background color
    :type color2_top: str
    :param color2_top_text: Top bar text color
    :type color2_top_text: str
    :param custom_namespace: Is this site using a custom namespace for users?
    :type custom_namespace: bool
    :param days_to_retain_backups: Number of days to keep deleted files
    :type days_to_retain_backups: int
    :param default_time_zone: Site default time zone
    :type default_time_zone: str
    :param desktop_app: Is the desktop app enabled?
    :type desktop_app: bool
    :param desktop_app_session_ip_pinning: Is desktop app session IP pinning enabled?
    :type desktop_app_session_ip_pinning: bool
    :param desktop_app_session_lifetime: Desktop app session lifetime (in hours)
    :type desktop_app_session_lifetime: int
    :param disable_2fa_with_delay: If set to true, we will begin the process of disabling 2FA on this site.
    :type disable_2fa_with_delay: bool
    :param disable_files_certificate_generation: If set, Files.com will not set the CAA records required to generate future SSL certificates for this domain.
    :type disable_files_certificate_generation: bool
    :param disable_password_reset: Is password reset disabled?
    :type disable_password_reset: bool
    :param disable_users_from_inactivity_period_days: If greater than zero, users will unable to login if they do not show activity within this number of days.
    :type disable_users_from_inactivity_period_days: int
    :param disallowed_countries: Comma seperated list of disallowed Country codes
    :type disallowed_countries: str
    :param domain: Custom domain
    :type domain: str
    :param domain_hsts_header: Send HSTS (HTTP Strict Transport Security) header when visitors access the site via a custom domain?
    :type domain_hsts_header: bool
    :param domain_letsencrypt_chain: Letsencrypt chain to use when registering SSL Certificate for domain.
    :type domain_letsencrypt_chain: str
    :param email: Main email for this site
    :type email: str
    :param folder_permissions_groups_only: If true, permissions for this site must be bound to a group (not a user). Otherwise, permissions must be bound to a user.
    :type folder_permissions_groups_only: bool
    :param ftp_enabled: Is FTP enabled?
    :type ftp_enabled: bool
    :param icon128_delete: If true, will delete the file stored in icon128
    :type icon128_delete: bool
    :param icon128_file: 
    :type icon128_file: str
    :param icon16_delete: If true, will delete the file stored in icon16
    :type icon16_delete: bool
    :param icon16_file: 
    :type icon16_file: str
    :param icon32_delete: If true, will delete the file stored in icon32
    :type icon32_delete: bool
    :param icon32_file: 
    :type icon32_file: str
    :param icon48_delete: If true, will delete the file stored in icon48
    :type icon48_delete: bool
    :param icon48_file: 
    :type icon48_file: str
    :param immutable_files: Are files protected from modification?
    :type immutable_files: bool
    :param include_password_in_welcome_email: Include password in emails to new users?
    :type include_password_in_welcome_email: bool
    :param language: Site default language
    :type language: str
    :param ldap_base_dn: Base DN for looking up users in LDAP server
    :type ldap_base_dn: str
    :param ldap_domain: Domain name that will be appended to usernames
    :type ldap_domain: str
    :param ldap_enabled: Main LDAP setting: is LDAP enabled?
    :type ldap_enabled: bool
    :param ldap_group_action: Should we sync groups from LDAP server?
    :type ldap_group_action: str
    :param ldap_group_exclusion: Comma or newline separated list of group names (with optional wildcards) to exclude when syncing.
    :type ldap_group_exclusion: str
    :param ldap_group_inclusion: Comma or newline separated list of group names (with optional wildcards) to include when syncing.
    :type ldap_group_inclusion: str
    :param ldap_host: LDAP host
    :type ldap_host: str
    :param ldap_host_2: LDAP backup host
    :type ldap_host_2: str
    :param ldap_host_3: LDAP backup host
    :type ldap_host_3: str
    :param ldap_password_change: New LDAP password.
    :type ldap_password_change: str
    :param ldap_password_change_confirmation: Confirm new LDAP password.
    :type ldap_password_change_confirmation: str
    :param ldap_port: LDAP port
    :type ldap_port: int
    :param ldap_secure: Use secure LDAP?
    :type ldap_secure: bool
    :param ldap_type: LDAP type
    :type ldap_type: str
    :param ldap_user_action: Should we sync users from LDAP server?
    :type ldap_user_action: str
    :param ldap_user_include_groups: Comma or newline separated list of group names (with optional wildcards) - if provided, only users in these groups will be added or synced.
    :type ldap_user_include_groups: str
    :param ldap_username: Username for signing in to LDAP server.
    :type ldap_username: str
    :param ldap_username_field: LDAP username field
    :type ldap_username_field: str
    :param login_help_text: Login help text
    :type login_help_text: str
    :param logo_delete: If true, will delete the file stored in logo
    :type logo_delete: bool
    :param logo_file: 
    :type logo_file: str
    :param max_prior_passwords: Number of prior passwords to disallow
    :type max_prior_passwords: int
    :param mobile_app: Is the mobile app enabled?
    :type mobile_app: bool
    :param mobile_app_session_ip_pinning: Is mobile app session IP pinning enabled?
    :type mobile_app_session_ip_pinning: bool
    :param mobile_app_session_lifetime: Mobile app session lifetime (in hours)
    :type mobile_app_session_lifetime: int
    :param motd_text: A message to show users when they connect via FTP or SFTP.
    :type motd_text: str
    :param motd_use_for_ftp: Show message to users connecting via FTP
    :type motd_use_for_ftp: bool
    :param motd_use_for_sftp: Show message to users connecting via SFTP
    :type motd_use_for_sftp: bool
    :param name: Site name
    :type name: str
    :param non_sso_groups_allowed: If true, groups can be manually created / modified / deleted by Site Admins. Otherwise, groups can only be managed via your SSO provider.
    :type non_sso_groups_allowed: bool
    :param non_sso_users_allowed: If true, users can be manually created / modified / deleted by Site Admins. Otherwise, users can only be managed via your SSO provider.
    :type non_sso_users_allowed: bool
    :param office_integration_available: Allow users to use Office for the web?
    :type office_integration_available: bool
    :param office_integration_type: Office integration application used to edit and view the MS Office documents
    :type office_integration_type: str
    :param opt_out_global: Use servers in the USA only?
    :type opt_out_global: bool
    :param password_min_length: Shortest password length for users
    :type password_min_length: int
    :param password_require_letter: Require a letter in passwords?
    :type password_require_letter: bool
    :param password_require_mixed: Require lower and upper case letters in passwords?
    :type password_require_mixed: bool
    :param password_require_number: Require a number in passwords?
    :type password_require_number: bool
    :param password_require_special: Require special characters in password?
    :type password_require_special: bool
    :param password_require_unbreached: Require passwords that have not been previously breached? (see https://haveibeenpwned.com/)
    :type password_require_unbreached: bool
    :param password_requirements_apply_to_bundles: Require bundles&#39; passwords, and passwords for other items (inboxes, public shares, etc.) to conform to the same requirements as users&#39; passwords?
    :type password_requirements_apply_to_bundles: bool
    :param password_validity_days: Number of days password is valid
    :type password_validity_days: int
    :param pin_all_remote_servers_to_site_region: If true, we will ensure that all internal communications with any remote server are made through the primary region of the site. This setting overrides individual remote server settings.
    :type pin_all_remote_servers_to_site_region: bool
    :param reply_to_email: Reply-to email for this site
    :type reply_to_email: str
    :param require_2fa: Require two-factor authentication for all users?
    :type require_2fa: bool
    :param require_2fa_user_type: What type of user is required to use two-factor authentication (when require_2fa is set to &#x60;true&#x60; for this site)?
    :type require_2fa_user_type: str
    :param session_expiry: Session expiry in hours
    :type session_expiry: float
    :param session_expiry_minutes: Session expiry in minutes
    :type session_expiry_minutes: int
    :param session_pinned_by_ip: Are sessions locked to the same IP? (i.e. do users need to log in again if they change IPs?)
    :type session_pinned_by_ip: bool
    :param sftp_enabled: Is SFTP enabled?
    :type sftp_enabled: bool
    :param sftp_host_key_type: Sftp Host Key Type
    :type sftp_host_key_type: str
    :param sftp_insecure_ciphers: Are Insecure Ciphers allowed for SFTP?  Note:  Settting TLS Disabled -&gt; True will always allow insecure ciphers for SFTP as well.  Enabling this is insecure.
    :type sftp_insecure_ciphers: bool
    :param sftp_user_root_enabled: Use user FTP roots also for SFTP?
    :type sftp_user_root_enabled: bool
    :param sharing_enabled: Allow bundle creation
    :type sharing_enabled: bool
    :param show_request_access_link: Show request access link for users without access?  Currently unused.
    :type show_request_access_link: bool
    :param site_footer: Custom site footer text
    :type site_footer: str
    :param site_header: Custom site header text
    :type site_header: str
    :param smtp_address: SMTP server hostname or IP
    :type smtp_address: str
    :param smtp_authentication: SMTP server authentication type
    :type smtp_authentication: str
    :param smtp_from: From address to use when mailing through custom SMTP
    :type smtp_from: str
    :param smtp_password: Password for SMTP server.
    :type smtp_password: str
    :param smtp_port: SMTP server port
    :type smtp_port: int
    :param smtp_username: SMTP server username
    :type smtp_username: str
    :param ssl_required: Is SSL required?  Disabling this is insecure.
    :type ssl_required: bool
    :param subdomain: Site subdomain
    :type subdomain: str
    :param tls_disabled: Are Insecure TLS and SFTP Ciphers allowed?  Enabling this is insecure.
    :type tls_disabled: bool
    :param uploads_via_email_authentication: Do incoming emails in the Inboxes require checking for SPF/DKIM/DMARC?
    :type uploads_via_email_authentication: bool
    :param use_provided_modified_at: Allow uploaders to set &#x60;provided_modified_at&#x60; for uploaded files?
    :type use_provided_modified_at: bool
    :param user_lockout: Will users be locked out after incorrect login attempts?
    :type user_lockout: bool
    :param user_lockout_lock_period: How many hours to lock user out for failed password?
    :type user_lockout_lock_period: int
    :param user_lockout_tries: Number of login tries within &#x60;user_lockout_within&#x60; hours before users are locked out
    :type user_lockout_tries: int
    :param user_lockout_within: Number of hours for user lockout window
    :type user_lockout_within: int
    :param user_requests_enabled: Enable User Requests feature
    :type user_requests_enabled: bool
    :param user_requests_notify_admins: Send email to site admins when a user request is received?
    :type user_requests_notify_admins: bool
    :param welcome_custom_text: Custom text send in user welcome email
    :type welcome_custom_text: str
    :param welcome_email_cc: Include this email in welcome emails if enabled
    :type welcome_email_cc: str
    :param welcome_email_enabled: Will the welcome email be sent to new users?
    :type welcome_email_enabled: bool
    :param welcome_email_subject: Include this email subject in welcome emails if enabled
    :type welcome_email_subject: str
    :param welcome_screen: Does the welcome screen appear?
    :type welcome_screen: str
    :param windows_mode_ftp: Does FTP user Windows emulation mode?
    :type windows_mode_ftp: bool

    """
    bundle_watermark_value = object.from_dict(bundle_watermark_value)
    return web.Response(status=200)


async def post_site_api_keys(request: web.Request, description=None, expires_at=None, name=None, path=None, permission_set=None, user_id=None) -> web.Response:
    """Create Api Key

    Create Api Key

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
    :param user_id: User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user.
    :type user_id: int

    """
    expires_at = util.deserialize_datetime(expires_at)
    return web.Response(status=200)


async def post_site_test_webhook(request: web.Request, url, action=None, body=None, encoding=None, headers=None, method=None) -> web.Response:
    """Test webhook.

    Test webhook.

    :param url: URL for testing the webhook.
    :type url: str
    :param action: action for test body
    :type action: str
    :param body: Additional body parameters.
    :type body: dict | bytes
    :param encoding: HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    :type encoding: str
    :param headers: Additional request headers.
    :type headers: dict | bytes
    :param method: HTTP method(GET or POST).
    :type method: str

    """
    body = object.from_dict(body)
    headers = object.from_dict(headers)
    return web.Response(status=200)
