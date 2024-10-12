# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.api_key_entity import ApiKeyEntity
from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server.models.public_key_entity import PublicKeyEntity
from openapi_server.models.user_entity import UserEntity


pytestmark = pytest.mark.asyncio

async def test_get_user_api_keys(client):
    """Test case for get_user_api_keys

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
        path='/api/rest/v1/user/api_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_groups(client):
    """Test case for get_user_groups

    List Group Users
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('group_id', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/user/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_public_keys(client):
    """Test case for get_user_public_keys

    List Public Keys
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/user/public_keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_user(client):
    """Test case for patch_user

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
        path='/api/rest/v1/user',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_user_api_keys(client):
    """Test case for post_user_api_keys

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
        path='/api/rest/v1/user/api_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_user_public_keys(client):
    """Test case for post_user_public_keys

    Create Public Key
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('public_key', 'public_key_example')
    data.add_field('title', 'title_example')
    data.add_field('user_id', 56)
    response = await client.request(
        method='POST',
        path='/api/rest/v1/user/public_keys',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

