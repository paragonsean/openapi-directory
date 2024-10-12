# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server.models.dns_record_entity import DnsRecordEntity
from openapi_server.models.ip_address_entity import IpAddressEntity
from openapi_server.models.site_entity import SiteEntity
from openapi_server.models.status_entity import StatusEntity
from openapi_server.models.usage_snapshot_entity import UsageSnapshotEntity


pytestmark = pytest.mark.asyncio

async def test_get_site(client):
    """Test case for get_site

    Show site settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/site',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_api_keys(client):
    """Test case for get_site_api_keys

    List Api Keys
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_lt', None),
                    ('filter_lteq', None)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/site/api_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_dns_records(client):
    """Test case for get_site_dns_records

    Show site DNS configuration.
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/site/dns_records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_ip_addresses(client):
    """Test case for get_site_ip_addresses

    List IP Addresses associated with the current site
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/site/ip_addresses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_usage(client):
    """Test case for get_site_usage

    Get the most recent usage snapshot (usage data for billing purposes) for a Site.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/site/usage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_site(client):
    """Test case for patch_site

    Update site settings.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('active_sftp_host_key_id', 56)
    data.add_field('allow_bundle_names', True)
    data.add_field('allowed_2fa_method_bypass_for_ftp_sftp_dav', True)
    data.add_field('allowed_2fa_method_sms', True)
    data.add_field('allowed_2fa_method_totp', True)
    data.add_field('allowed_2fa_method_u2f', True)
    data.add_field('allowed_2fa_method_webauthn', True)
    data.add_field('allowed_2fa_method_yubi', True)
    data.add_field('allowed_countries', 'allowed_countries_example')
    data.add_field('allowed_ips', 'allowed_ips_example')
    data.add_field('ask_about_overwrites', True)
    data.add_field('bundle_activity_notifications', 'bundle_activity_notifications_example')
    data.add_field('bundle_expiration', 56)
    data.add_field('bundle_password_required', True)
    data.add_field('bundle_registration_notifications', 'bundle_registration_notifications_example')
    data.add_field('bundle_require_share_recipient', True)
    data.add_field('bundle_upload_receipt_notifications', 'bundle_upload_receipt_notifications_example')
    data.add_field('bundle_watermark_attachment_delete', True)
    data.add_field('bundle_watermark_attachment_file', '/path/to/file')
    data.add_field('bundle_watermark_value', None)
    data.add_field('color2_left', 'color2_left_example')
    data.add_field('color2_link', 'color2_link_example')
    data.add_field('color2_text', 'color2_text_example')
    data.add_field('color2_top', 'color2_top_example')
    data.add_field('color2_top_text', 'color2_top_text_example')
    data.add_field('custom_namespace', True)
    data.add_field('days_to_retain_backups', 56)
    data.add_field('default_time_zone', 'default_time_zone_example')
    data.add_field('desktop_app', True)
    data.add_field('desktop_app_session_ip_pinning', True)
    data.add_field('desktop_app_session_lifetime', 56)
    data.add_field('disable_2fa_with_delay', True)
    data.add_field('disable_files_certificate_generation', True)
    data.add_field('disable_password_reset', True)
    data.add_field('disable_users_from_inactivity_period_days', 56)
    data.add_field('disallowed_countries', 'disallowed_countries_example')
    data.add_field('domain', 'domain_example')
    data.add_field('domain_hsts_header', True)
    data.add_field('domain_letsencrypt_chain', 'domain_letsencrypt_chain_example')
    data.add_field('email', 'email_example')
    data.add_field('folder_permissions_groups_only', True)
    data.add_field('ftp_enabled', True)
    data.add_field('icon128_delete', True)
    data.add_field('icon128_file', '/path/to/file')
    data.add_field('icon16_delete', True)
    data.add_field('icon16_file', '/path/to/file')
    data.add_field('icon32_delete', True)
    data.add_field('icon32_file', '/path/to/file')
    data.add_field('icon48_delete', True)
    data.add_field('icon48_file', '/path/to/file')
    data.add_field('immutable_files', True)
    data.add_field('include_password_in_welcome_email', True)
    data.add_field('language', 'language_example')
    data.add_field('ldap_base_dn', 'ldap_base_dn_example')
    data.add_field('ldap_domain', 'ldap_domain_example')
    data.add_field('ldap_enabled', True)
    data.add_field('ldap_group_action', 'ldap_group_action_example')
    data.add_field('ldap_group_exclusion', 'ldap_group_exclusion_example')
    data.add_field('ldap_group_inclusion', 'ldap_group_inclusion_example')
    data.add_field('ldap_host', 'ldap_host_example')
    data.add_field('ldap_host_2', 'ldap_host_2_example')
    data.add_field('ldap_host_3', 'ldap_host_3_example')
    data.add_field('ldap_password_change', 'ldap_password_change_example')
    data.add_field('ldap_password_change_confirmation', 'ldap_password_change_confirmation_example')
    data.add_field('ldap_port', 56)
    data.add_field('ldap_secure', True)
    data.add_field('ldap_type', 'ldap_type_example')
    data.add_field('ldap_user_action', 'ldap_user_action_example')
    data.add_field('ldap_user_include_groups', 'ldap_user_include_groups_example')
    data.add_field('ldap_username', 'ldap_username_example')
    data.add_field('ldap_username_field', 'ldap_username_field_example')
    data.add_field('login_help_text', 'login_help_text_example')
    data.add_field('logo_delete', True)
    data.add_field('logo_file', '/path/to/file')
    data.add_field('max_prior_passwords', 56)
    data.add_field('mobile_app', True)
    data.add_field('mobile_app_session_ip_pinning', True)
    data.add_field('mobile_app_session_lifetime', 56)
    data.add_field('motd_text', 'motd_text_example')
    data.add_field('motd_use_for_ftp', True)
    data.add_field('motd_use_for_sftp', True)
    data.add_field('name', 'name_example')
    data.add_field('non_sso_groups_allowed', True)
    data.add_field('non_sso_users_allowed', True)
    data.add_field('office_integration_available', True)
    data.add_field('office_integration_type', 'office_integration_type_example')
    data.add_field('opt_out_global', True)
    data.add_field('password_min_length', 56)
    data.add_field('password_require_letter', True)
    data.add_field('password_require_mixed', True)
    data.add_field('password_require_number', True)
    data.add_field('password_require_special', True)
    data.add_field('password_require_unbreached', True)
    data.add_field('password_requirements_apply_to_bundles', True)
    data.add_field('password_validity_days', 56)
    data.add_field('pin_all_remote_servers_to_site_region', True)
    data.add_field('reply_to_email', 'reply_to_email_example')
    data.add_field('require_2fa', True)
    data.add_field('require_2fa_user_type', 'require_2fa_user_type_example')
    data.add_field('session_expiry', 3.4)
    data.add_field('session_expiry_minutes', 56)
    data.add_field('session_pinned_by_ip', True)
    data.add_field('sftp_enabled', True)
    data.add_field('sftp_host_key_type', 'sftp_host_key_type_example')
    data.add_field('sftp_insecure_ciphers', True)
    data.add_field('sftp_user_root_enabled', True)
    data.add_field('sharing_enabled', True)
    data.add_field('show_request_access_link', True)
    data.add_field('site_footer', 'site_footer_example')
    data.add_field('site_header', 'site_header_example')
    data.add_field('smtp_address', 'smtp_address_example')
    data.add_field('smtp_authentication', 'smtp_authentication_example')
    data.add_field('smtp_from', 'smtp_from_example')
    data.add_field('smtp_password', 'smtp_password_example')
    data.add_field('smtp_port', 56)
    data.add_field('smtp_username', 'smtp_username_example')
    data.add_field('ssl_required', True)
    data.add_field('subdomain', 'subdomain_example')
    data.add_field('tls_disabled', True)
    data.add_field('uploads_via_email_authentication', True)
    data.add_field('use_provided_modified_at', True)
    data.add_field('user_lockout', True)
    data.add_field('user_lockout_lock_period', 56)
    data.add_field('user_lockout_tries', 56)
    data.add_field('user_lockout_within', 56)
    data.add_field('user_requests_enabled', True)
    data.add_field('user_requests_notify_admins', True)
    data.add_field('welcome_custom_text', 'welcome_custom_text_example')
    data.add_field('welcome_email_cc', 'welcome_email_cc_example')
    data.add_field('welcome_email_enabled', True)
    data.add_field('welcome_email_subject', 'welcome_email_subject_example')
    data.add_field('welcome_screen', 'welcome_screen_example')
    data.add_field('windows_mode_ftp', True)
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/site',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_site_api_keys(client):
    """Test case for post_site_api_keys

    Create Api Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('description', 'description_example')
    data.add_field('expires_at', '2013-10-20T19:20:30+01:00')
    data.add_field('name', 'name_example')
    data.add_field('path', 'path_example')
    data.add_field('permission_set', full)
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/site/api_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_site_test_webhook(client):
    """Test case for post_site_test_webhook

    Test webhook.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('action', 'action_example')
    data.add_field('body', None)
    data.add_field('encoding', 'encoding_example')
    data.add_field('headers', None)
    data.add_field('method', 'method_example')
    data.add_field('url', 'url_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/site/test-webhook',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

