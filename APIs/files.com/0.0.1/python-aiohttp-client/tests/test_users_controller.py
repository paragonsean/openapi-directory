# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server.models.permission_entity import PermissionEntity
from openapi_server.models.public_key_entity import PublicKeyEntity
from openapi_server.models.user_cipher_use_entity import UserCipherUseEntity
from openapi_server.models.user_entity import UserEntity


pytestmark = pytest.mark.asyncio

async def test_delete_users_id(client):
    """Test case for delete_users_id

    Delete User
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    List Users
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_gt', None),
                    ('filter_gteq', None),
                    ('filter_prefix', None),
                    ('filter_lt', None),
                    ('filter_lteq', None),
                    ('ids', 'ids_example'),
                    ('q[username]', 'q_username_example'),
                    ('q[email]', 'q_email_example'),
                    ('q[notes]', 'q_notes_example'),
                    ('q[admin]', 'q_admin_example'),
                    ('q[allowed_ips]', 'q_allowed_ips_example'),
                    ('q[password_validity_days]', 'q_password_validity_days_example'),
                    ('q[ssl_required]', 'q_ssl_required_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_id(client):
    """Test case for get_users_id

    Show User
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_api_keys(client):
    """Test case for get_users_user_id_api_keys

    List Api Keys
    """
    params = [('cursor', 'cursor_example'),
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
        path='/api/rest/v1/users/{user_id}/api_keys'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_cipher_uses(client):
    """Test case for get_users_user_id_cipher_uses

    List User Cipher Uses
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users/{user_id}/cipher_uses'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_groups(client):
    """Test case for get_users_user_id_groups

    List Group Users
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('group_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users/{user_id}/groups'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_permissions(client):
    """Test case for get_users_user_id_permissions

    List Permissions
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('path', 'path_example'),
                    ('group_id', 'group_id_example'),
                    ('include_groups', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users/{user_id}/permissions'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_user_id_public_keys(client):
    """Test case for get_users_user_id_public_keys

    List Public Keys
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/users/{user_id}/public_keys'.format(user_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_users_id(client):
    """Test case for patch_users_id

    Update User
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allowed_ips', 'allowed_ips_example')
    data.add_field('announcements_read', True)
    data.add_field('attachments_permission', True)
    data.add_field('authenticate_until', '2013-10-20T19:20:30+01:00')
    data.add_field('authentication_method', 'authentication_method_example')
    data.add_field('avatar_delete', True)
    data.add_field('avatar_file', '/path/to/file')
    data.add_field('billing_permission', True)
    data.add_field('bypass_inactive_disable', True)
    data.add_field('bypass_site_allowed_ips', True)
    data.add_field('change_password', 'change_password_example')
    data.add_field('change_password_confirmation', 'change_password_confirmation_example')
    data.add_field('company', 'company_example')
    data.add_field('dav_permission', True)
    data.add_field('disabled', True)
    data.add_field('email', 'email_example')
    data.add_field('ftp_permission', True)
    data.add_field('grant_permission', 'grant_permission_example')
    data.add_field('group_id', 56)
    data.add_field('group_ids', 'group_ids_example')
    data.add_field('header_text', 'header_text_example')
    data.add_field('imported_password_hash', 'imported_password_hash_example')
    data.add_field('language', 'language_example')
    data.add_field('name', 'name_example')
    data.add_field('notes', 'notes_example')
    data.add_field('notification_daily_send_time', 56)
    data.add_field('office_integration_enabled', True)
    data.add_field('password', 'password_example')
    data.add_field('password_confirmation', 'password_confirmation_example')
    data.add_field('password_validity_days', 56)
    data.add_field('receive_admin_alerts', True)
    data.add_field('require_2fa', 'require_2fa_example')
    data.add_field('require_password_change', True)
    data.add_field('restapi_permission', True)
    data.add_field('self_managed', True)
    data.add_field('sftp_permission', True)
    data.add_field('site_admin', True)
    data.add_field('skip_welcome_screen', True)
    data.add_field('ssl_required', 'ssl_required_example')
    data.add_field('sso_strategy_id', 56)
    data.add_field('subscribe_to_newsletter', True)
    data.add_field('time_zone', 'time_zone_example')
    data.add_field('user_root', 'user_root_example')
    data.add_field('username', 'username_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/users/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_users(client):
    """Test case for post_users

    Create User
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('allowed_ips', 'allowed_ips_example')
    data.add_field('announcements_read', True)
    data.add_field('attachments_permission', True)
    data.add_field('authenticate_until', '2013-10-20T19:20:30+01:00')
    data.add_field('authentication_method', 'authentication_method_example')
    data.add_field('avatar_delete', True)
    data.add_field('avatar_file', '/path/to/file')
    data.add_field('billing_permission', True)
    data.add_field('bypass_inactive_disable', True)
    data.add_field('bypass_site_allowed_ips', True)
    data.add_field('change_password', 'change_password_example')
    data.add_field('change_password_confirmation', 'change_password_confirmation_example')
    data.add_field('company', 'company_example')
    data.add_field('dav_permission', True)
    data.add_field('disabled', True)
    data.add_field('email', 'email_example')
    data.add_field('ftp_permission', True)
    data.add_field('grant_permission', 'grant_permission_example')
    data.add_field('group_id', 56)
    data.add_field('group_ids', 'group_ids_example')
    data.add_field('header_text', 'header_text_example')
    data.add_field('imported_password_hash', 'imported_password_hash_example')
    data.add_field('language', 'language_example')
    data.add_field('name', 'name_example')
    data.add_field('notes', 'notes_example')
    data.add_field('notification_daily_send_time', 56)
    data.add_field('office_integration_enabled', True)
    data.add_field('password', 'password_example')
    data.add_field('password_confirmation', 'password_confirmation_example')
    data.add_field('password_validity_days', 56)
    data.add_field('receive_admin_alerts', True)
    data.add_field('require_2fa', 'require_2fa_example')
    data.add_field('require_password_change', True)
    data.add_field('restapi_permission', True)
    data.add_field('self_managed', True)
    data.add_field('sftp_permission', True)
    data.add_field('site_admin', True)
    data.add_field('skip_welcome_screen', True)
    data.add_field('ssl_required', 'ssl_required_example')
    data.add_field('sso_strategy_id', 56)
    data.add_field('subscribe_to_newsletter', True)
    data.add_field('time_zone', 'time_zone_example')
    data.add_field('user_root', 'user_root_example')
    data.add_field('username', 'username_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_id2fa_reset(client):
    """Test case for post_users_id2fa_reset

    Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users/{id}/2fa/reset'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_id_resend_welcome_email(client):
    """Test case for post_users_id_resend_welcome_email

    Resend user welcome email
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users/{id}/resend_welcome_email'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_users_id_unlock(client):
    """Test case for post_users_id_unlock

    Unlock user who has been locked out due to failed logins.
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users/{id}/unlock'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_users_user_id_api_keys(client):
    """Test case for post_users_user_id_api_keys

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
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users/{user_id}/api_keys'.format(user_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_users_user_id_public_keys(client):
    """Test case for post_users_user_id_public_keys

    Create Public Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('public_key', 'public_key_example')
    data.add_field('title', 'title_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/users/{user_id}/public_keys'.format(user_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

