# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_conversations_archive_error_schema import AdminConversationsArchiveErrorSchema
from openapi_server.models.admin_conversations_archive_schema import AdminConversationsArchiveSchema
from openapi_server.models.admin_conversations_convert_to_private_error_schema import AdminConversationsConvertToPrivateErrorSchema
from openapi_server.models.admin_conversations_convert_to_private_schema import AdminConversationsConvertToPrivateSchema
from openapi_server.models.admin_conversations_create_error_schema import AdminConversationsCreateErrorSchema
from openapi_server.models.admin_conversations_create_schema import AdminConversationsCreateSchema
from openapi_server.models.admin_conversations_delete_error_schema import AdminConversationsDeleteErrorSchema
from openapi_server.models.admin_conversations_delete_schema import AdminConversationsDeleteSchema
from openapi_server.models.admin_conversations_disconnect_shared_error_schema import AdminConversationsDisconnectSharedErrorSchema
from openapi_server.models.admin_conversations_get_conversation_prefs_schema import AdminConversationsGetConversationPrefsSchema
from openapi_server.models.admin_conversations_get_teams_error_schema import AdminConversationsGetTeamsErrorSchema
from openapi_server.models.admin_conversations_get_teams_schema import AdminConversationsGetTeamsSchema
from openapi_server.models.admin_conversations_invite_error_schema import AdminConversationsInviteErrorSchema
from openapi_server.models.admin_conversations_invite_schema import AdminConversationsInviteSchema
from openapi_server.models.admin_conversations_rename_schema import AdminConversationsRenameSchema
from openapi_server.models.admin_conversations_rename_schema1 import AdminConversationsRenameSchema1
from openapi_server.models.admin_conversations_search_error_schema import AdminConversationsSearchErrorSchema
from openapi_server.models.admin_conversations_search_schema import AdminConversationsSearchSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_error_schema import AdminConversationsSetConversationPrefsErrorSchema
from openapi_server.models.admin_conversations_set_conversation_prefs_schema import AdminConversationsSetConversationPrefsSchema
from openapi_server.models.admin_conversations_unarchive_error_schema import AdminConversationsUnarchiveErrorSchema
from openapi_server.models.admin_conversations_unarchive_error_schema1 import AdminConversationsUnarchiveErrorSchema1
from openapi_server.models.admin_conversations_unarchive_error_schema2 import AdminConversationsUnarchiveErrorSchema2
from openapi_server.models.admin_conversations_unarchive_schema import AdminConversationsUnarchiveSchema
from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_apps_approve_0(client):
    """Test case for admin_apps_approve_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'app_id': 'app_id_example',
        'request_id': 'request_id_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.apps.approve',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_apps_approved_list_0(client):
    """Test case for admin_apps_approved_list_0

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('team_id', 'team_id_example'),
                    ('enterprise_id', 'enterprise_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.apps.approved.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_apps_requests_list_0(client):
    """Test case for admin_apps_requests_list_0

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.apps.requests.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_apps_restrict_0(client):
    """Test case for admin_apps_restrict_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'app_id': 'app_id_example',
        'request_id': 'request_id_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.apps.restrict',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_apps_restricted_list_0(client):
    """Test case for admin_apps_restricted_list_0

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('team_id', 'team_id_example'),
                    ('enterprise_id', 'enterprise_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.apps.restricted.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_archive_0(client):
    """Test case for admin_conversations_archive_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.archive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_convert_to_private_0(client):
    """Test case for admin_conversations_convert_to_private_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.convertToPrivate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_create_0(client):
    """Test case for admin_conversations_create_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'is_private': True,
        'name': 'name_example',
        'org_wide': True,
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_delete_0(client):
    """Test case for admin_conversations_delete_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.delete',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_disconnect_shared_0(client):
    """Test case for admin_conversations_disconnect_shared_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'leaving_team_ids': 'leaving_team_ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.disconnectShared',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_ekm_list_original_connected_channel_info_0(client):
    """Test case for admin_conversations_ekm_list_original_connected_channel_info_0

    
    """
    params = [('token', 'token_example'),
                    ('channel_ids', 'channel_ids_example'),
                    ('team_ids', 'team_ids_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.ekm.listOriginalConnectedChannelInfo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_get_conversation_prefs_0(client):
    """Test case for admin_conversations_get_conversation_prefs_0

    
    """
    params = [('channel_id', 'channel_id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.getConversationPrefs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_get_teams_0(client):
    """Test case for admin_conversations_get_teams_0

    
    """
    params = [('channel_id', 'channel_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.getTeams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_invite_0(client):
    """Test case for admin_conversations_invite_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'user_ids': 'user_ids_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.invite',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_rename_0(client):
    """Test case for admin_conversations_rename_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'name': 'name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.rename',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_restrict_access_add_group_0(client):
    """Test case for admin_conversations_restrict_access_add_group_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'group_id': 'group_id_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.restrictAccess.addGroup',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_restrict_access_list_groups_0(client):
    """Test case for admin_conversations_restrict_access_list_groups_0

    
    """
    params = [('token', 'token_example'),
                    ('channel_id', 'channel_id_example'),
                    ('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.restrictAccess.listGroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_restrict_access_remove_group_0(client):
    """Test case for admin_conversations_restrict_access_remove_group_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'group_id': 'group_id_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.restrictAccess.removeGroup',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_conversations_search_0(client):
    """Test case for admin_conversations_search_0

    
    """
    params = [('team_ids', 'team_ids_example'),
                    ('query', 'query_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('search_channel_types', 'search_channel_types_example'),
                    ('sort', 'sort_example'),
                    ('sort_dir', 'sort_dir_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.conversations.search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_set_conversation_prefs_0(client):
    """Test case for admin_conversations_set_conversation_prefs_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'prefs': 'prefs_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.setConversationPrefs',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_set_teams_0(client):
    """Test case for admin_conversations_set_teams_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example',
        'org_channel': True,
        'target_team_ids': 'target_team_ids_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.setTeams',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_conversations_unarchive_0(client):
    """Test case for admin_conversations_unarchive_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_id': 'channel_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.conversations.unarchive',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_emoji_add_0(client):
    """Test case for admin_emoji_add_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'token': 'token_example',
        'url': 'url_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.emoji.add',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_emoji_add_alias_0(client):
    """Test case for admin_emoji_add_alias_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'alias_for': 'alias_for_example',
        'name': 'name_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.emoji.addAlias',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_emoji_list_0(client):
    """Test case for admin_emoji_list_0

    
    """
    params = [('token', 'token_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.emoji.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_emoji_remove_0(client):
    """Test case for admin_emoji_remove_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.emoji.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_emoji_rename_0(client):
    """Test case for admin_emoji_rename_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'new_name': 'new_name_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.emoji.rename',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_invite_requests_approve_0(client):
    """Test case for admin_invite_requests_approve_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'invite_request_id': 'invite_request_id_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.inviteRequests.approve',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_invite_requests_approved_list_0(client):
    """Test case for admin_invite_requests_approved_list_0

    
    """
    params = [('team_id', 'team_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.inviteRequests.approved.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_invite_requests_denied_list_0(client):
    """Test case for admin_invite_requests_denied_list_0

    
    """
    params = [('team_id', 'team_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.inviteRequests.denied.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_invite_requests_deny_0(client):
    """Test case for admin_invite_requests_deny_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'invite_request_id': 'invite_request_id_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.inviteRequests.deny',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_invite_requests_list_0(client):
    """Test case for admin_invite_requests_list_0

    
    """
    params = [('team_id', 'team_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.inviteRequests.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_teams_admins_list_0(client):
    """Test case for admin_teams_admins_list_0

    
    """
    params = [('token', 'token_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example'),
                    ('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.teams.admins.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_create_0(client):
    """Test case for admin_teams_create_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_description': 'team_description_example',
        'team_discoverability': 'team_discoverability_example',
        'team_domain': 'team_domain_example',
        'team_name': 'team_name_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.create',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_teams_list_0(client):
    """Test case for admin_teams_list_0

    
    """
    params = [('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.teams.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_teams_owners_list_0(client):
    """Test case for admin_teams_owners_list_0

    
    """
    params = [('token', 'token_example'),
                    ('team_id', 'team_id_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.teams.owners.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_teams_settings_info_0(client):
    """Test case for admin_teams_settings_info_0

    
    """
    params = [('team_id', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.teams.settings.info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_default_channels_0(client):
    """Test case for admin_teams_settings_set_default_channels_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDefaultChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_description_0(client):
    """Test case for admin_teams_settings_set_description_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'description': 'description_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDescription',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_discoverability_0(client):
    """Test case for admin_teams_settings_set_discoverability_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'discoverability': 'discoverability_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setDiscoverability',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_icon_0(client):
    """Test case for admin_teams_settings_set_icon_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'image_url': 'image_url_example',
        'team_id': 'team_id_example',
        'token': 'token_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setIcon',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_teams_settings_set_name_0(client):
    """Test case for admin_teams_settings_set_name_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'name': 'name_example',
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.teams.settings.setName',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_add_channels_0(client):
    """Test case for admin_usergroups_add_channels_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'team_id': 'team_id_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.addChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_add_teams_0(client):
    """Test case for admin_usergroups_add_teams_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'auto_provision': True,
        'team_ids': 'team_ids_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.addTeams',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_usergroups_list_channels_0(client):
    """Test case for admin_usergroups_list_channels_0

    
    """
    params = [('usergroup_id', 'usergroup_id_example'),
                    ('team_id', 'team_id_example'),
                    ('include_num_members', True)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.usergroups.listChannels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_usergroups_remove_channels_0(client):
    """Test case for admin_usergroups_remove_channels_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'usergroup_id': 'usergroup_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.usergroups.removeChannels',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_assign_0(client):
    """Test case for admin_users_assign_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'is_restricted': True,
        'is_ultra_restricted': True,
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.assign',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_invite_0(client):
    """Test case for admin_users_invite_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'channel_ids': 'channel_ids_example',
        'custom_message': 'custom_message_example',
        'email': 'email_example',
        'guest_expiration_ts': 'guest_expiration_ts_example',
        'is_restricted': True,
        'is_ultra_restricted': True,
        'real_name': 'real_name_example',
        'resend': True,
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.invite',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_users_list_0(client):
    """Test case for admin_users_list_0

    
    """
    params = [('team_id', 'team_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/admin.users.list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_remove_0(client):
    """Test case for admin_users_remove_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.remove',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_session_invalidate_0(client):
    """Test case for admin_users_session_invalidate_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'session_id': 56,
        'team_id': 'team_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.session.invalidate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_session_reset_0(client):
    """Test case for admin_users_session_reset_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'mobile_only': True,
        'user_id': 'user_id_example',
        'web_only': True
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.session.reset',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_admin_0(client):
    """Test case for admin_users_set_admin_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setAdmin',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_expiration_0(client):
    """Test case for admin_users_set_expiration_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'expiration_ts': 56,
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setExpiration',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_owner_0(client):
    """Test case for admin_users_set_owner_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setOwner',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_admin_users_set_regular_0(client):
    """Test case for admin_users_set_regular_0

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'token': 'token_example',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'team_id': 'team_id_example',
        'user_id': 'user_id_example'
        }
    response = await client.request(
        method='POST',
        path='/api/admin.users.setRegular',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

