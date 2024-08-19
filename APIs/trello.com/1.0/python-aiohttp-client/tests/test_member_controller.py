# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.members import Members
from openapi_server.models.members_avatar import MembersAvatar
from openapi_server.models.members_avatar_source import MembersAvatarSource
from openapi_server.models.members_bio import MembersBio
from openapi_server.models.members_board_backgrounds import MembersBoardBackgrounds
from openapi_server.models.members_board_stars import MembersBoardStars
from openapi_server.models.members_board_stars_id_board import MembersBoardStarsIdBoard
from openapi_server.models.members_board_stars_pos import MembersBoardStarsPos
from openapi_server.models.members_custom_board_backgrounds import MembersCustomBoardBackgrounds
from openapi_server.models.members_custom_emoji import MembersCustomEmoji
from openapi_server.models.members_custom_stickers import MembersCustomStickers
from openapi_server.models.members_full_name import MembersFullName
from openapi_server.models.members_initials import MembersInitials
from openapi_server.models.members_one_time_messages_dismissed import MembersOneTimeMessagesDismissed
from openapi_server.models.members_saved_searches import MembersSavedSearches
from openapi_server.models.members_saved_searches_name import MembersSavedSearchesName
from openapi_server.models.members_saved_searches_pos import MembersSavedSearchesPos
from openapi_server.models.members_saved_searches_query import MembersSavedSearchesQuery
from openapi_server.models.members_username import MembersUsername
from openapi_server.models.prefs_color_blind import PrefsColorBlind
from openapi_server.models.prefs_locale import PrefsLocale
from openapi_server.models.prefs_minutes_between_summaries import PrefsMinutesBetweenSummaries


pytestmark = pytest.mark.asyncio

async def test_add_members_avatar_by_id_member(client):
    """Test case for add_members_avatar_by_id_member

    addMembersAvatarByIdMember()
    """
    body = openapi_server.MembersAvatar()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/avatar'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_board_backgrounds_by_id_member(client):
    """Test case for add_members_board_backgrounds_by_id_member

    addMembersBoardBackgroundsByIdMember()
    """
    body = openapi_server.MembersBoardBackgrounds()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/boardBackgrounds'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_board_stars_by_id_member(client):
    """Test case for add_members_board_stars_by_id_member

    addMembersBoardStarsByIdMember()
    """
    body = openapi_server.MembersBoardStars()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/boardStars'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_custom_board_backgrounds_by_id_member(client):
    """Test case for add_members_custom_board_backgrounds_by_id_member

    addMembersCustomBoardBackgroundsByIdMember()
    """
    body = openapi_server.MembersCustomBoardBackgrounds()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/customBoardBackgrounds'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_custom_emoji_by_id_member(client):
    """Test case for add_members_custom_emoji_by_id_member

    addMembersCustomEmojiByIdMember()
    """
    body = openapi_server.MembersCustomEmoji()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/customEmoji'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_custom_stickers_by_id_member(client):
    """Test case for add_members_custom_stickers_by_id_member

    addMembersCustomStickersByIdMember()
    """
    body = openapi_server.MembersCustomStickers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/customStickers'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_one_time_messages_dismissed_by_id_member(client):
    """Test case for add_members_one_time_messages_dismissed_by_id_member

    addMembersOneTimeMessagesDismissedByIdMember()
    """
    body = openapi_server.MembersOneTimeMessagesDismissed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/oneTimeMessagesDismissed'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_members_saved_searches_by_id_member(client):
    """Test case for add_members_saved_searches_by_id_member

    addMembersSavedSearchesByIdMember()
    """
    body = openapi_server.MembersSavedSearches()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/members/{id_member}/savedSearches'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_members_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for delete_members_board_backgrounds_by_id_member_by_id_board_background

    deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/members/{id_member}/boardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_members_board_stars_by_id_member_by_id_board_star(client):
    """Test case for delete_members_board_stars_by_id_member_by_id_board_star

    deleteMembersBoardStarsByIdMemberByIdBoardStar()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/members/{id_member}/boardStars/{id_board_star}'.format(id_member='id_member_example', id_board_star='id_board_star_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_members_custom_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for delete_members_custom_board_backgrounds_by_id_member_by_id_board_background

    deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/members/{id_member}/customBoardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_members_custom_stickers_by_id_member_by_id_custom_sticker(client):
    """Test case for delete_members_custom_stickers_by_id_member_by_id_custom_sticker

    deleteMembersCustomStickersByIdMemberByIdCustomSticker()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/members/{id_member}/customStickers/{id_custom_sticker}'.format(id_member='id_member_example', id_custom_sticker='id_custom_sticker_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_members_saved_searches_by_id_member_by_id_saved_search(client):
    """Test case for delete_members_saved_searches_by_id_member_by_id_saved_search

    deleteMembersSavedSearchesByIdMemberByIdSavedSearch()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_actions_by_id_member(client):
    """Test case for get_members_actions_by_id_member

    getMembersActionsByIdMember()
    """
    params = [('entities', 'entities_example'),
                    ('display', 'display_example'),
                    ('filter', 'all'),
                    ('fields', 'all'),
                    ('limit', '50'),
                    ('format', 'list'),
                    ('since', 'since_example'),
                    ('before', 'before_example'),
                    ('page', '0'),
                    ('idModels', 'id_models_example'),
                    ('member', 'member_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('memberCreator', 'member_creator_example'),
                    ('memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/actions'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_board_backgrounds_by_id_member(client):
    """Test case for get_members_board_backgrounds_by_id_member

    getMembersBoardBackgroundsByIdMember()
    """
    params = [('filter', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardBackgrounds'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for get_members_board_backgrounds_by_id_member_by_id_board_background

    getMembersBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_board_stars_by_id_member(client):
    """Test case for get_members_board_stars_by_id_member

    getMembersBoardStarsByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardStars'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_board_stars_by_id_member_by_id_board_star(client):
    """Test case for get_members_board_stars_by_id_member_by_id_board_star

    getMembersBoardStarsByIdMemberByIdBoardStar()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardStars/{id_board_star}'.format(id_member='id_member_example', id_board_star='id_board_star_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_boards_by_id_member(client):
    """Test case for get_members_boards_by_id_member

    getMembersBoardsByIdMember()
    """
    params = [('filter', 'all'),
                    ('fields', 'all'),
                    ('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_limit', '50'),
                    ('actions_format', 'list'),
                    ('actions_since', 'actions_since_example'),
                    ('action_fields', 'all'),
                    ('memberships', 'none'),
                    ('organization', 'organization_example'),
                    ('organization_fields', 'name and displayName'),
                    ('lists', 'none'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boards'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_boards_by_id_member_by_filter(client):
    """Test case for get_members_boards_by_id_member_by_filter

    getMembersBoardsByIdMemberByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boards/{filter}'.format(id_member='id_member_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_boards_invited_by_id_member(client):
    """Test case for get_members_boards_invited_by_id_member

    getMembersBoardsInvitedByIdMember()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardsInvited'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_boards_invited_by_id_member_by_field(client):
    """Test case for get_members_boards_invited_by_id_member_by_field

    getMembersBoardsInvitedByIdMemberByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/boardsInvited/{_field}'.format(id_member='id_member_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_by_id_member(client):
    """Test case for get_members_by_id_member

    getMembersByIdMember()
    """
    params = [('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_display', 'actions_display_example'),
                    ('actions_limit', '50'),
                    ('action_fields', 'all'),
                    ('action_since', 'action_since_example'),
                    ('action_before', 'action_before_example'),
                    ('cards', 'none'),
                    ('card_fields', 'all'),
                    ('card_members', 'card_members_example'),
                    ('card_member_fields', 'avatarHash, fullName, initials and username'),
                    ('card_attachments', 'card_attachments_example'),
                    ('card_attachment_fields', 'url and previews'),
                    ('card_stickers', 'card_stickers_example'),
                    ('boards', 'boards_example'),
                    ('board_fields', 'name, closed, idOrganization and pinned'),
                    ('board_actions', 'board_actions_example'),
                    ('board_actions_entities', 'board_actions_entities_example'),
                    ('board_actions_display', 'board_actions_display_example'),
                    ('board_actions_format', 'list'),
                    ('board_actions_since', 'board_actions_since_example'),
                    ('board_actions_limit', '50'),
                    ('board_action_fields', 'all'),
                    ('board_lists', 'none'),
                    ('board_memberships', 'none'),
                    ('board_organization', 'board_organization_example'),
                    ('board_organization_fields', 'name and displayName'),
                    ('boardsInvited', 'boards_invited_example'),
                    ('boardsInvited_fields', 'name, closed, idOrganization and pinned'),
                    ('boardStars', 'board_stars_example'),
                    ('savedSearches', 'saved_searches_example'),
                    ('organizations', 'none'),
                    ('organization_fields', 'all'),
                    ('organization_paid_account', 'organization_paid_account_example'),
                    ('organizationsInvited', 'none'),
                    ('organizationsInvited_fields', 'all'),
                    ('notifications', 'notifications_example'),
                    ('notifications_entities', 'notifications_entities_example'),
                    ('notifications_display', 'notifications_display_example'),
                    ('notifications_limit', '50'),
                    ('notification_fields', 'all'),
                    ('notification_memberCreator', 'notification_member_creator_example'),
                    ('notification_memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('notification_before', 'notification_before_example'),
                    ('notification_since', 'notification_since_example'),
                    ('tokens', 'none'),
                    ('paid_account', 'paid_account_example'),
                    ('boardBackgrounds', 'none'),
                    ('customBoardBackgrounds', 'none'),
                    ('customStickers', 'none'),
                    ('customEmoji', 'none'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_by_id_member_by_field(client):
    """Test case for get_members_by_id_member_by_field

    getMembersByIdMemberByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/{_field}'.format(id_member='id_member_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_cards_by_id_member(client):
    """Test case for get_members_cards_by_id_member

    getMembersCardsByIdMember()
    """
    params = [('actions', 'actions_example'),
                    ('attachments', 'attachments_example'),
                    ('attachment_fields', 'all'),
                    ('stickers', 'stickers_example'),
                    ('members', 'members_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('checkItemStates', 'check_item_states_example'),
                    ('checklists', 'none'),
                    ('limit', 'limit_example'),
                    ('since', 'since_example'),
                    ('before', 'before_example'),
                    ('filter', 'visible'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/cards'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_cards_by_id_member_by_filter(client):
    """Test case for get_members_cards_by_id_member_by_filter

    getMembersCardsByIdMemberByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/cards/{filter}'.format(id_member='id_member_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_board_backgrounds_by_id_member(client):
    """Test case for get_members_custom_board_backgrounds_by_id_member

    getMembersCustomBoardBackgroundsByIdMember()
    """
    params = [('filter', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customBoardBackgrounds'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for get_members_custom_board_backgrounds_by_id_member_by_id_board_background

    getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customBoardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_emoji_by_id_member(client):
    """Test case for get_members_custom_emoji_by_id_member

    getMembersCustomEmojiByIdMember()
    """
    params = [('filter', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customEmoji'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_emoji_by_id_member_by_id_custom_emoji(client):
    """Test case for get_members_custom_emoji_by_id_member_by_id_custom_emoji

    getMembersCustomEmojiByIdMemberByIdCustomEmoji()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customEmoji/{id_custom_emoji}'.format(id_member='id_member_example', id_custom_emoji='id_custom_emoji_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_stickers_by_id_member(client):
    """Test case for get_members_custom_stickers_by_id_member

    getMembersCustomStickersByIdMember()
    """
    params = [('filter', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customStickers'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_custom_stickers_by_id_member_by_id_custom_sticker(client):
    """Test case for get_members_custom_stickers_by_id_member_by_id_custom_sticker

    getMembersCustomStickersByIdMemberByIdCustomSticker()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/customStickers/{id_custom_sticker}'.format(id_member='id_member_example', id_custom_sticker='id_custom_sticker_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_deltas_by_id_member(client):
    """Test case for get_members_deltas_by_id_member

    getMembersDeltasByIdMember()
    """
    params = [('tags', 'tags_example'),
                    ('ixLastUpdate', 'ix_last_update_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/deltas'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_notifications_by_id_member(client):
    """Test case for get_members_notifications_by_id_member

    getMembersNotificationsByIdMember()
    """
    params = [('entities', 'entities_example'),
                    ('display', 'display_example'),
                    ('filter', 'all'),
                    ('read_filter', 'all'),
                    ('fields', 'all'),
                    ('limit', '50'),
                    ('page', '0'),
                    ('before', 'before_example'),
                    ('since', 'since_example'),
                    ('memberCreator', 'member_creator_example'),
                    ('memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/notifications'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_notifications_by_id_member_by_filter(client):
    """Test case for get_members_notifications_by_id_member_by_filter

    getMembersNotificationsByIdMemberByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/notifications/{filter}'.format(id_member='id_member_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_organizations_by_id_member(client):
    """Test case for get_members_organizations_by_id_member

    getMembersOrganizationsByIdMember()
    """
    params = [('filter', 'all'),
                    ('fields', 'all'),
                    ('paid_account', 'paid_account_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/organizations'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_organizations_by_id_member_by_filter(client):
    """Test case for get_members_organizations_by_id_member_by_filter

    getMembersOrganizationsByIdMemberByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/organizations/{filter}'.format(id_member='id_member_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_organizations_invited_by_id_member(client):
    """Test case for get_members_organizations_invited_by_id_member

    getMembersOrganizationsInvitedByIdMember()
    """
    params = [('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/organizationsInvited'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_organizations_invited_by_id_member_by_field(client):
    """Test case for get_members_organizations_invited_by_id_member_by_field

    getMembersOrganizationsInvitedByIdMemberByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/organizationsInvited/{_field}'.format(id_member='id_member_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_saved_searches_by_id_member(client):
    """Test case for get_members_saved_searches_by_id_member

    getMembersSavedSearchesByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/savedSearches'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_saved_searches_by_id_member_by_id_saved_search(client):
    """Test case for get_members_saved_searches_by_id_member_by_id_saved_search

    getMembersSavedSearchesByIdMemberByIdSavedSearch()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_members_tokens_by_id_member(client):
    """Test case for get_members_tokens_by_id_member

    getMembersTokensByIdMember()
    """
    params = [('filter', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/members/{id_member}/tokens'.format(id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_avatar_source_by_id_member(client):
    """Test case for update_members_avatar_source_by_id_member

    updateMembersAvatarSourceByIdMember()
    """
    body = openapi_server.MembersAvatarSource()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/avatarSource'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_bio_by_id_member(client):
    """Test case for update_members_bio_by_id_member

    updateMembersBioByIdMember()
    """
    body = openapi_server.MembersBio()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/bio'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for update_members_board_backgrounds_by_id_member_by_id_board_background

    updateMembersBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    body = openapi_server.MembersBoardBackgrounds()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/boardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_board_stars_by_id_member_by_id_board_star(client):
    """Test case for update_members_board_stars_by_id_member_by_id_board_star

    updateMembersBoardStarsByIdMemberByIdBoardStar()
    """
    body = openapi_server.MembersBoardStars()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/boardStars/{id_board_star}'.format(id_member='id_member_example', id_board_star='id_board_star_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_board_stars_id_board_by_id_member_by_id_board_star(client):
    """Test case for update_members_board_stars_id_board_by_id_member_by_id_board_star

    updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar()
    """
    body = openapi_server.MembersBoardStarsIdBoard()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/boardStars/{id_board_star}/idBoard'.format(id_member='id_member_example', id_board_star='id_board_star_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_board_stars_pos_by_id_member_by_id_board_star(client):
    """Test case for update_members_board_stars_pos_by_id_member_by_id_board_star

    updateMembersBoardStarsPosByIdMemberByIdBoardStar()
    """
    body = openapi_server.MembersBoardStarsPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/boardStars/{id_board_star}/pos'.format(id_member='id_member_example', id_board_star='id_board_star_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_by_id_member(client):
    """Test case for update_members_by_id_member

    updateMembersByIdMember()
    """
    body = openapi_server.Members()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_custom_board_backgrounds_by_id_member_by_id_board_background(client):
    """Test case for update_members_custom_board_backgrounds_by_id_member_by_id_board_background

    updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()
    """
    body = openapi_server.MembersCustomBoardBackgrounds()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/customBoardBackgrounds/{id_board_background}'.format(id_member='id_member_example', id_board_background='id_board_background_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_full_name_by_id_member(client):
    """Test case for update_members_full_name_by_id_member

    updateMembersFullNameByIdMember()
    """
    body = openapi_server.MembersFullName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/fullName'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_initials_by_id_member(client):
    """Test case for update_members_initials_by_id_member

    updateMembersInitialsByIdMember()
    """
    body = openapi_server.MembersInitials()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/initials'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_prefs_color_blind_by_id_member(client):
    """Test case for update_members_prefs_color_blind_by_id_member

    updateMembersPrefsColorBlindByIdMember()
    """
    body = openapi_server.PrefsColorBlind()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/prefs/colorBlind'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_prefs_locale_by_id_member(client):
    """Test case for update_members_prefs_locale_by_id_member

    updateMembersPrefsLocaleByIdMember()
    """
    body = openapi_server.PrefsLocale()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/prefs/locale'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_prefs_minutes_between_summaries_by_id_member(client):
    """Test case for update_members_prefs_minutes_between_summaries_by_id_member

    updateMembersPrefsMinutesBetweenSummariesByIdMember()
    """
    body = openapi_server.PrefsMinutesBetweenSummaries()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/prefs/minutesBetweenSummaries'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_saved_searches_by_id_member_by_id_saved_search(client):
    """Test case for update_members_saved_searches_by_id_member_by_id_saved_search

    updateMembersSavedSearchesByIdMemberByIdSavedSearch()
    """
    body = openapi_server.MembersSavedSearches()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_saved_searches_name_by_id_member_by_id_saved_search(client):
    """Test case for update_members_saved_searches_name_by_id_member_by_id_saved_search

    updateMembersSavedSearchesNameByIdMemberByIdSavedSearch()
    """
    body = openapi_server.MembersSavedSearchesName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}/name'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_saved_searches_pos_by_id_member_by_id_saved_search(client):
    """Test case for update_members_saved_searches_pos_by_id_member_by_id_saved_search

    updateMembersSavedSearchesPosByIdMemberByIdSavedSearch()
    """
    body = openapi_server.MembersSavedSearchesPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}/pos'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_saved_searches_query_by_id_member_by_id_saved_search(client):
    """Test case for update_members_saved_searches_query_by_id_member_by_id_saved_search

    updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch()
    """
    body = openapi_server.MembersSavedSearchesQuery()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/savedSearches/{id_saved_search}/query'.format(id_member='id_member_example', id_saved_search='id_saved_search_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_members_username_by_id_member(client):
    """Test case for update_members_username_by_id_member

    updateMembersUsernameByIdMember()
    """
    body = openapi_server.MembersUsername()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/members/{id_member}/username'.format(id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

