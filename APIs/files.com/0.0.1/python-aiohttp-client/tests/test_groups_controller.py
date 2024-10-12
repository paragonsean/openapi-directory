# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.group_entity import GroupEntity
from openapi_server.models.group_user_entity import GroupUserEntity
from openapi_server.models.permission_entity import PermissionEntity
from openapi_server.models.user_entity import UserEntity


pytestmark = pytest.mark.asyncio

async def test_delete_groups_group_id_memberships_user_id(client):
    """Test case for delete_groups_group_id_memberships_user_id

    Delete Group User
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/groups/{group_id}/memberships/{user_id}'.format(group_id=56, user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_groups_id(client):
    """Test case for delete_groups_id

    Delete Group
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups(client):
    """Test case for get_groups

    List Groups
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('ids', 'ids_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups_group_id_permissions(client):
    """Test case for get_groups_group_id_permissions

    List Permissions
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('filter', None),
                    ('filter_prefix', None),
                    ('path', 'path_example'),
                    ('user_id', 'user_id_example'),
                    ('include_groups', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/groups/{group_id}/permissions'.format(group_id='group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups_group_id_users(client):
    """Test case for get_groups_group_id_users

    List Group Users
    """
    params = [('user_id', 56),
                    ('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/groups/{group_id}/users'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_groups_id(client):
    """Test case for get_groups_id

    Show Group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_groups_group_id_memberships_user_id(client):
    """Test case for patch_groups_group_id_memberships_user_id

    Update Group User
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('admin', True)
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/groups/{group_id}/memberships/{user_id}'.format(group_id=56, user_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_groups_id(client):
    """Test case for patch_groups_id

    Update Group
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('admin_ids', 'admin_ids_example')
    data.add_field('name', 'name_example')
    data.add_field('notes', 'notes_example')
    data.add_field('user_ids', 'user_ids_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/groups/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_groups(client):
    """Test case for post_groups

    Create Group
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('admin_ids', 'admin_ids_example')
    data.add_field('name', 'name_example')
    data.add_field('notes', 'notes_example')
    data.add_field('user_ids', 'user_ids_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/groups',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_groups_group_id_users(client):
    """Test case for post_groups_group_id_users

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
        path='/api/rest/v1/groups/{group_id}/users'.format(group_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

