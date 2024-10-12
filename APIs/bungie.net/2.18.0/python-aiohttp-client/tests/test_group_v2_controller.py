# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.destiny2_equip_item200_response import Destiny2EquipItem200Response
from openapi_server.models.forum_get_topic_for_content200_response import ForumGetTopicForContent200Response
from openapi_server.models.get_available_locales200_response import GetAvailableLocales200Response
from openapi_server.models.group_v2_approve_all_pending200_response import GroupV2ApproveAllPending200Response
from openapi_server.models.group_v2_get_admins_and_founder_of_group200_response import GroupV2GetAdminsAndFounderOfGroup200Response
from openapi_server.models.group_v2_get_available_themes200_response import GroupV2GetAvailableThemes200Response
from openapi_server.models.group_v2_get_banned_members_of_group200_response import GroupV2GetBannedMembersOfGroup200Response
from openapi_server.models.group_v2_get_group_by_name200_response import GroupV2GetGroupByName200Response
from openapi_server.models.group_v2_get_group_optional_conversations200_response import GroupV2GetGroupOptionalConversations200Response
from openapi_server.models.group_v2_get_groups_for_member200_response import GroupV2GetGroupsForMember200Response
from openapi_server.models.group_v2_get_invited_individuals200_response import GroupV2GetInvitedIndividuals200Response
from openapi_server.models.group_v2_get_potential_groups_for_member200_response import GroupV2GetPotentialGroupsForMember200Response
from openapi_server.models.group_v2_get_recommended_groups200_response import GroupV2GetRecommendedGroups200Response
from openapi_server.models.group_v2_get_user_clan_invite_setting200_response import GroupV2GetUserClanInviteSetting200Response
from openapi_server.models.group_v2_group_search200_response import GroupV2GroupSearch200Response
from openapi_server.models.group_v2_individual_group_invite200_response import GroupV2IndividualGroupInvite200Response
from openapi_server.models.group_v2_kick_member200_response import GroupV2KickMember200Response
from openapi_server.models.group_v2_recover_group_for_founder200_response import GroupV2RecoverGroupForFounder200Response


pytestmark = pytest.mark.asyncio

async def test_group_v2_abdicate_foundership(client):
    """Test case for group_v2_abdicate_foundership

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Admin/AbdicateFoundership/{membership_type}/{founder_id_new}'.format(founder_id_new=56, group_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_add_optional_conversation(client):
    """Test case for group_v2_add_optional_conversation

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/OptionalConversations/Add'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_approve_all_pending(client):
    """Test case for group_v2_approve_all_pending

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/ApproveAll'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_approve_pending(client):
    """Test case for group_v2_approve_pending

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/Approve/{membership_type}/{membership_id}'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_approve_pending_for_list(client):
    """Test case for group_v2_approve_pending_for_list

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/ApproveList'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_ban_member(client):
    """Test case for group_v2_ban_member

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Ban'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_deny_all_pending(client):
    """Test case for group_v2_deny_all_pending

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/DenyAll'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_deny_pending_for_list(client):
    """Test case for group_v2_deny_pending_for_list

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/DenyList'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_edit_clan_banner(client):
    """Test case for group_v2_edit_clan_banner

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/EditClanBanner'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_edit_founder_options(client):
    """Test case for group_v2_edit_founder_options

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/EditFounderOptions'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_edit_group(client):
    """Test case for group_v2_edit_group

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Edit'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_edit_group_membership(client):
    """Test case for group_v2_edit_group_membership

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/SetMembershipType/{member_type}'.format(group_id=56, membership_id=56, membership_type=56, member_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_edit_optional_conversation(client):
    """Test case for group_v2_edit_optional_conversation

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/OptionalConversations/Edit/{conversation_id}'.format(conversation_id=56, group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_admins_and_founder_of_group(client):
    """Test case for group_v2_get_admins_and_founder_of_group

    
    """
    params = [('currentpage', 56)]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/AdminsAndFounder'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_available_avatars(client):
    """Test case for group_v2_get_available_avatars

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/GetAvailableAvatars/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_available_themes(client):
    """Test case for group_v2_get_available_themes

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/GetAvailableThemes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_banned_members_of_group(client):
    """Test case for group_v2_get_banned_members_of_group

    
    """
    params = [('currentpage', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/Banned'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_group(client):
    """Test case for group_v2_get_group

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_group_by_name(client):
    """Test case for group_v2_get_group_by_name

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/Name/{group_name}/{group_type}'.format(group_name='group_name_example', group_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_group_by_name_v2(client):
    """Test case for group_v2_get_group_by_name_v2

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/NameV2/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_group_optional_conversations(client):
    """Test case for group_v2_get_group_optional_conversations

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/OptionalConversations'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_groups_for_member(client):
    """Test case for group_v2_get_groups_for_member

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/User/{membership_type}/{membership_id}/{filter}/{group_type}'.format(filter=56, group_type=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_invited_individuals(client):
    """Test case for group_v2_get_invited_individuals

    
    """
    params = [('currentpage', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/Members/InvitedIndividuals'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_members_of_group(client):
    """Test case for group_v2_get_members_of_group

    
    """
    params = [('currentpage', 56),
                    ('memberType', 56),
                    ('nameSearch', 'name_search_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/Members'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_pending_memberships(client):
    """Test case for group_v2_get_pending_memberships

    
    """
    params = [('currentpage', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/{group_id}/Members/Pending'.format(group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_potential_groups_for_member(client):
    """Test case for group_v2_get_potential_groups_for_member

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/User/Potential/{membership_type}/{membership_id}/{filter}/{group_type}'.format(filter=56, group_type=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_recommended_groups(client):
    """Test case for group_v2_get_recommended_groups

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/Recommended/{group_type}/{create_date_range}'.format(create_date_range=56, group_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_get_user_clan_invite_setting(client):
    """Test case for group_v2_get_user_clan_invite_setting

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/GetUserClanInviteSetting/{m_type}'.format(m_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_group_search(client):
    """Test case for group_v2_group_search

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/Search/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_individual_group_invite(client):
    """Test case for group_v2_individual_group_invite

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/IndividualInvite/{membership_type}/{membership_id}'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_individual_group_invite_cancel(client):
    """Test case for group_v2_individual_group_invite_cancel

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/IndividualInviteCancel/{membership_type}/{membership_id}'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_kick_member(client):
    """Test case for group_v2_kick_member

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Kick'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_recover_group_for_founder(client):
    """Test case for group_v2_recover_group_for_founder

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/Platform/GroupV2/Recover/{membership_type}/{membership_id}/{group_type}'.format(group_type=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_group_v2_unban_member(client):
    """Test case for group_v2_unban_member

    
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Platform/GroupV2/{group_id}/Members/{membership_type}/{membership_id}/Unban'.format(group_id=56, membership_id=56, membership_type=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

