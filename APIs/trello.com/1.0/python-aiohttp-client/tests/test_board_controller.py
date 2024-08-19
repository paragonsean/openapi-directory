# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.boards import Boards
from openapi_server.models.boards_checklists import BoardsChecklists
from openapi_server.models.boards_closed import BoardsClosed
from openapi_server.models.boards_desc import BoardsDesc
from openapi_server.models.boards_id_organization import BoardsIdOrganization
from openapi_server.models.boards_labels import BoardsLabels
from openapi_server.models.boards_lists import BoardsLists
from openapi_server.models.boards_members import BoardsMembers
from openapi_server.models.boards_memberships import BoardsMemberships
from openapi_server.models.boards_name import BoardsName
from openapi_server.models.boards_power_ups import BoardsPowerUps
from openapi_server.models.boards_subscribed import BoardsSubscribed
from openapi_server.models.label_names_blue import LabelNamesBlue
from openapi_server.models.label_names_green import LabelNamesGreen
from openapi_server.models.label_names_orange import LabelNamesOrange
from openapi_server.models.label_names_purple import LabelNamesPurple
from openapi_server.models.label_names_red import LabelNamesRed
from openapi_server.models.label_names_yellow import LabelNamesYellow
from openapi_server.models.my_prefs_email_position import MyPrefsEmailPosition
from openapi_server.models.my_prefs_id_email_list import MyPrefsIdEmailList
from openapi_server.models.my_prefs_show_list_guide import MyPrefsShowListGuide
from openapi_server.models.my_prefs_show_sidebar import MyPrefsShowSidebar
from openapi_server.models.my_prefs_show_sidebar_activity import MyPrefsShowSidebarActivity
from openapi_server.models.my_prefs_show_sidebar_board_actions import MyPrefsShowSidebarBoardActions
from openapi_server.models.my_prefs_show_sidebar_members import MyPrefsShowSidebarMembers
from openapi_server.models.prefs_background import PrefsBackground
from openapi_server.models.prefs_calendar_feed_enabled import PrefsCalendarFeedEnabled
from openapi_server.models.prefs_card_aging import PrefsCardAging
from openapi_server.models.prefs_card_covers import PrefsCardCovers
from openapi_server.models.prefs_comments import PrefsComments
from openapi_server.models.prefs_invitations import PrefsInvitations
from openapi_server.models.prefs_permission_level import PrefsPermissionLevel
from openapi_server.models.prefs_self_join import PrefsSelfJoin
from openapi_server.models.prefs_voting import PrefsVoting


pytestmark = pytest.mark.asyncio

async def test_add_boards(client):
    """Test case for add_boards

    addBoards()
    """
    body = openapi_server.Boards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_calendar_key_generate_by_id_board(client):
    """Test case for add_boards_calendar_key_generate_by_id_board

    addBoardsCalendarKeyGenerateByIdBoard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/calendarKey/generate'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_checklists_by_id_board(client):
    """Test case for add_boards_checklists_by_id_board

    addBoardsChecklistsByIdBoard()
    """
    body = openapi_server.BoardsChecklists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/checklists'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_email_key_generate_by_id_board(client):
    """Test case for add_boards_email_key_generate_by_id_board

    addBoardsEmailKeyGenerateByIdBoard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/emailKey/generate'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_labels_by_id_board(client):
    """Test case for add_boards_labels_by_id_board

    addBoardsLabelsByIdBoard()
    """
    body = openapi_server.BoardsLabels()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/labels'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_lists_by_id_board(client):
    """Test case for add_boards_lists_by_id_board

    addBoardsListsByIdBoard()
    """
    body = openapi_server.BoardsLists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/lists'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_mark_as_viewed_by_id_board(client):
    """Test case for add_boards_mark_as_viewed_by_id_board

    addBoardsMarkAsViewedByIdBoard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/markAsViewed'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_boards_power_ups_by_id_board(client):
    """Test case for add_boards_power_ups_by_id_board

    addBoardsPowerUpsByIdBoard()
    """
    body = openapi_server.BoardsPowerUps()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/boards/{id_board}/powerUps'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_boards_members_by_id_board_by_id_member(client):
    """Test case for delete_boards_members_by_id_board_by_id_member

    deleteBoardsMembersByIdBoardByIdMember()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/boards/{id_board}/members/{id_member}'.format(id_board='id_board_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_boards_power_ups_by_id_board_by_power_up(client):
    """Test case for delete_boards_power_ups_by_id_board_by_power_up

    deleteBoardsPowerUpsByIdBoardByPowerUp()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/boards/{id_board}/powerUps/{power_up}'.format(id_board='id_board_example', power_up='power_up_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_actions_by_id_board(client):
    """Test case for get_boards_actions_by_id_board

    getBoardsActionsByIdBoard()
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
        path='/1/boards/{id_board}/actions'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_board_stars_by_id_board(client):
    """Test case for get_boards_board_stars_by_id_board

    getBoardsBoardStarsByIdBoard()
    """
    params = [('filter', 'mine'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/boardStars'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_by_id_board(client):
    """Test case for get_boards_by_id_board

    getBoardsByIdBoard()
    """
    params = [('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_display', 'actions_display_example'),
                    ('actions_format', 'list'),
                    ('actions_since', 'actions_since_example'),
                    ('actions_limit', '50'),
                    ('action_fields', 'all'),
                    ('action_member', 'action_member_example'),
                    ('action_member_fields', 'avatarHash, fullName, initials and username'),
                    ('action_memberCreator', 'action_member_creator_example'),
                    ('action_memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('cards', 'none'),
                    ('card_fields', 'all'),
                    ('card_attachments', 'card_attachments_example'),
                    ('card_attachment_fields', 'all'),
                    ('card_checklists', 'none'),
                    ('card_stickers', 'card_stickers_example'),
                    ('boardStars', 'none'),
                    ('labels', 'none'),
                    ('label_fields', 'all'),
                    ('labels_limit', '50'),
                    ('lists', 'none'),
                    ('list_fields', 'all'),
                    ('memberships', 'none'),
                    ('memberships_member', 'memberships_member_example'),
                    ('memberships_member_fields', 'fullName and username'),
                    ('members', 'none'),
                    ('member_fields', 'avatarHash, initials, fullName, username and confirmed'),
                    ('membersInvited', 'none'),
                    ('membersInvited_fields', 'avatarHash, initials, fullName and username'),
                    ('checklists', 'none'),
                    ('checklist_fields', 'all'),
                    ('organization', 'organization_example'),
                    ('organization_fields', 'name and displayName'),
                    ('organization_memberships', 'none'),
                    ('myPrefs', 'my_prefs_example'),
                    ('fields', 'name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_by_id_board_by_field(client):
    """Test case for get_boards_by_id_board_by_field

    getBoardsByIdBoardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/{_field}'.format(id_board='id_board_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_cards_by_id_board(client):
    """Test case for get_boards_cards_by_id_board

    getBoardsCardsByIdBoard()
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
        path='/1/boards/{id_board}/cards'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_cards_by_id_board_by_filter(client):
    """Test case for get_boards_cards_by_id_board_by_filter

    getBoardsCardsByIdBoardByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/cards/{filter}'.format(id_board='id_board_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_cards_by_id_board_by_id_card(client):
    """Test case for get_boards_cards_by_id_board_by_id_card

    getBoardsCardsByIdBoardByIdCard()
    """
    params = [('attachments', 'attachments_example'),
                    ('attachment_fields', 'all'),
                    ('actions', 'actions_example'),
                    ('actions_entities', 'actions_entities_example'),
                    ('actions_display', 'actions_display_example'),
                    ('actions_limit', '50'),
                    ('action_fields', 'all'),
                    ('action_memberCreator_fields', 'avatarHash, fullName, initials and username'),
                    ('members', 'members_example'),
                    ('member_fields', 'avatarHash, initials, fullName and username'),
                    ('checkItemStates', 'check_item_states_example'),
                    ('checkItemState_fields', 'all'),
                    ('labels', 'labels_example'),
                    ('checklists', 'none'),
                    ('checklist_fields', 'all'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/cards/{id_card}'.format(id_board='id_board_example', id_card='id_card_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_checklists_by_id_board(client):
    """Test case for get_boards_checklists_by_id_board

    getBoardsChecklistsByIdBoard()
    """
    params = [('cards', 'none'),
                    ('card_fields', 'all'),
                    ('checkItems', 'all'),
                    ('checkItem_fields', 'name, nameData, pos and state'),
                    ('filter', 'all'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/checklists'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_deltas_by_id_board(client):
    """Test case for get_boards_deltas_by_id_board

    getBoardsDeltasByIdBoard()
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
        path='/1/boards/{id_board}/deltas'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_labels_by_id_board(client):
    """Test case for get_boards_labels_by_id_board

    getBoardsLabelsByIdBoard()
    """
    params = [('fields', 'all'),
                    ('limit', '50'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/labels'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_labels_by_id_board_by_id_label(client):
    """Test case for get_boards_labels_by_id_board_by_id_label

    getBoardsLabelsByIdBoardByIdLabel()
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
        path='/1/boards/{id_board}/labels/{id_label}'.format(id_board='id_board_example', id_label='id_label_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_lists_by_id_board(client):
    """Test case for get_boards_lists_by_id_board

    getBoardsListsByIdBoard()
    """
    params = [('cards', 'none'),
                    ('card_fields', 'all'),
                    ('filter', 'open'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/lists'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_lists_by_id_board_by_filter(client):
    """Test case for get_boards_lists_by_id_board_by_filter

    getBoardsListsByIdBoardByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/lists/{filter}'.format(id_board='id_board_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_members_by_id_board(client):
    """Test case for get_boards_members_by_id_board

    getBoardsMembersByIdBoard()
    """
    params = [('filter', 'all'),
                    ('fields', 'fullName and username'),
                    ('activity', 'activity_example'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/members'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_members_by_id_board_by_filter(client):
    """Test case for get_boards_members_by_id_board_by_filter

    getBoardsMembersByIdBoardByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/members/{filter}'.format(id_board='id_board_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_members_cards_by_id_board_by_id_member(client):
    """Test case for get_boards_members_cards_by_id_board_by_id_member

    getBoardsMembersCardsByIdBoardByIdMember()
    """
    params = [('actions', 'actions_example'),
                    ('attachments', 'attachments_example'),
                    ('attachment_fields', 'all'),
                    ('members', 'members_example'),
                    ('member_fields', 'avatarHash, fullName, initials and username'),
                    ('checkItemStates', 'check_item_states_example'),
                    ('checklists', 'none'),
                    ('board', 'board_example'),
                    ('board_fields', 'name, desc, closed, idOrganization, pinned, url and prefs'),
                    ('list', 'list_example'),
                    ('list_fields', 'all'),
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
        path='/1/boards/{id_board}/members/{id_member}/cards'.format(id_board='id_board_example', id_member='id_member_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_members_invited_by_id_board(client):
    """Test case for get_boards_members_invited_by_id_board

    getBoardsMembersInvitedByIdBoard()
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
        path='/1/boards/{id_board}/membersInvited'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_members_invited_by_id_board_by_field(client):
    """Test case for get_boards_members_invited_by_id_board_by_field

    getBoardsMembersInvitedByIdBoardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/membersInvited/{_field}'.format(id_board='id_board_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_memberships_by_id_board(client):
    """Test case for get_boards_memberships_by_id_board

    getBoardsMembershipsByIdBoard()
    """
    params = [('filter', 'all'),
                    ('member', 'member_example'),
                    ('member_fields', 'fullName and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/memberships'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_memberships_by_id_board_by_id_membership(client):
    """Test case for get_boards_memberships_by_id_board_by_id_membership

    getBoardsMembershipsByIdBoardByIdMembership()
    """
    params = [('member', 'member_example'),
                    ('member_fields', 'fullName and username'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/memberships/{id_membership}'.format(id_board='id_board_example', id_membership='id_membership_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_my_prefs_by_id_board(client):
    """Test case for get_boards_my_prefs_by_id_board

    getBoardsMyPrefsByIdBoard()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/myPrefs'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_organization_by_id_board(client):
    """Test case for get_boards_organization_by_id_board

    getBoardsOrganizationByIdBoard()
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
        path='/1/boards/{id_board}/organization'.format(id_board='id_board_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_boards_organization_by_id_board_by_field(client):
    """Test case for get_boards_organization_by_id_board_by_field

    getBoardsOrganizationByIdBoardByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/boards/{id_board}/organization/{_field}'.format(id_board='id_board_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_by_id_board(client):
    """Test case for update_boards_by_id_board

    updateBoardsByIdBoard()
    """
    body = openapi_server.Boards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_closed_by_id_board(client):
    """Test case for update_boards_closed_by_id_board

    updateBoardsClosedByIdBoard()
    """
    body = openapi_server.BoardsClosed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/closed'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_desc_by_id_board(client):
    """Test case for update_boards_desc_by_id_board

    updateBoardsDescByIdBoard()
    """
    body = openapi_server.BoardsDesc()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/desc'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_id_organization_by_id_board(client):
    """Test case for update_boards_id_organization_by_id_board

    updateBoardsIdOrganizationByIdBoard()
    """
    body = openapi_server.BoardsIdOrganization()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/idOrganization'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_blue_by_id_board(client):
    """Test case for update_boards_label_names_blue_by_id_board

    updateBoardsLabelNamesBlueByIdBoard()
    """
    body = openapi_server.LabelNamesBlue()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/blue'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_green_by_id_board(client):
    """Test case for update_boards_label_names_green_by_id_board

    updateBoardsLabelNamesGreenByIdBoard()
    """
    body = openapi_server.LabelNamesGreen()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/green'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_orange_by_id_board(client):
    """Test case for update_boards_label_names_orange_by_id_board

    updateBoardsLabelNamesOrangeByIdBoard()
    """
    body = openapi_server.LabelNamesOrange()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/orange'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_purple_by_id_board(client):
    """Test case for update_boards_label_names_purple_by_id_board

    updateBoardsLabelNamesPurpleByIdBoard()
    """
    body = openapi_server.LabelNamesPurple()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/purple'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_red_by_id_board(client):
    """Test case for update_boards_label_names_red_by_id_board

    updateBoardsLabelNamesRedByIdBoard()
    """
    body = openapi_server.LabelNamesRed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/red'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_label_names_yellow_by_id_board(client):
    """Test case for update_boards_label_names_yellow_by_id_board

    updateBoardsLabelNamesYellowByIdBoard()
    """
    body = openapi_server.LabelNamesYellow()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/labelNames/yellow'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_members_by_id_board(client):
    """Test case for update_boards_members_by_id_board

    updateBoardsMembersByIdBoard()
    """
    body = openapi_server.BoardsMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/members'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_members_by_id_board_by_id_member(client):
    """Test case for update_boards_members_by_id_board_by_id_member

    updateBoardsMembersByIdBoardByIdMember()
    """
    body = openapi_server.BoardsMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/members/{id_member}'.format(id_board='id_board_example', id_member='id_member_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_memberships_by_id_board_by_id_membership(client):
    """Test case for update_boards_memberships_by_id_board_by_id_membership

    updateBoardsMembershipsByIdBoardByIdMembership()
    """
    body = openapi_server.BoardsMemberships()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/memberships/{id_membership}'.format(id_board='id_board_example', id_membership='id_membership_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_email_position_by_id_board(client):
    """Test case for update_boards_my_prefs_email_position_by_id_board

    updateBoardsMyPrefsEmailPositionByIdBoard()
    """
    body = openapi_server.MyPrefsEmailPosition()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/emailPosition'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_id_email_list_by_id_board(client):
    """Test case for update_boards_my_prefs_id_email_list_by_id_board

    updateBoardsMyPrefsIdEmailListByIdBoard()
    """
    body = openapi_server.MyPrefsIdEmailList()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/idEmailList'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_show_list_guide_by_id_board(client):
    """Test case for update_boards_my_prefs_show_list_guide_by_id_board

    updateBoardsMyPrefsShowListGuideByIdBoard()
    """
    body = openapi_server.MyPrefsShowListGuide()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/showListGuide'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_show_sidebar_activity_by_id_board(client):
    """Test case for update_boards_my_prefs_show_sidebar_activity_by_id_board

    updateBoardsMyPrefsShowSidebarActivityByIdBoard()
    """
    body = openapi_server.MyPrefsShowSidebarActivity()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/showSidebarActivity'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_show_sidebar_board_actions_by_id_board(client):
    """Test case for update_boards_my_prefs_show_sidebar_board_actions_by_id_board

    updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()
    """
    body = openapi_server.MyPrefsShowSidebarBoardActions()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/showSidebarBoardActions'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_show_sidebar_by_id_board(client):
    """Test case for update_boards_my_prefs_show_sidebar_by_id_board

    updateBoardsMyPrefsShowSidebarByIdBoard()
    """
    body = openapi_server.MyPrefsShowSidebar()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/showSidebar'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_my_prefs_show_sidebar_members_by_id_board(client):
    """Test case for update_boards_my_prefs_show_sidebar_members_by_id_board

    updateBoardsMyPrefsShowSidebarMembersByIdBoard()
    """
    body = openapi_server.MyPrefsShowSidebarMembers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/myPrefs/showSidebarMembers'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_name_by_id_board(client):
    """Test case for update_boards_name_by_id_board

    updateBoardsNameByIdBoard()
    """
    body = openapi_server.BoardsName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/name'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_background_by_id_board(client):
    """Test case for update_boards_prefs_background_by_id_board

    updateBoardsPrefsBackgroundByIdBoard()
    """
    body = openapi_server.PrefsBackground()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/background'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_calendar_feed_enabled_by_id_board(client):
    """Test case for update_boards_prefs_calendar_feed_enabled_by_id_board

    updateBoardsPrefsCalendarFeedEnabledByIdBoard()
    """
    body = openapi_server.PrefsCalendarFeedEnabled()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/calendarFeedEnabled'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_card_aging_by_id_board(client):
    """Test case for update_boards_prefs_card_aging_by_id_board

    updateBoardsPrefsCardAgingByIdBoard()
    """
    body = openapi_server.PrefsCardAging()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/cardAging'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_card_covers_by_id_board(client):
    """Test case for update_boards_prefs_card_covers_by_id_board

    updateBoardsPrefsCardCoversByIdBoard()
    """
    body = openapi_server.PrefsCardCovers()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/cardCovers'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_comments_by_id_board(client):
    """Test case for update_boards_prefs_comments_by_id_board

    updateBoardsPrefsCommentsByIdBoard()
    """
    body = openapi_server.PrefsComments()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/comments'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_invitations_by_id_board(client):
    """Test case for update_boards_prefs_invitations_by_id_board

    updateBoardsPrefsInvitationsByIdBoard()
    """
    body = openapi_server.PrefsInvitations()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/invitations'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_permission_level_by_id_board(client):
    """Test case for update_boards_prefs_permission_level_by_id_board

    updateBoardsPrefsPermissionLevelByIdBoard()
    """
    body = openapi_server.PrefsPermissionLevel()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/permissionLevel'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_self_join_by_id_board(client):
    """Test case for update_boards_prefs_self_join_by_id_board

    updateBoardsPrefsSelfJoinByIdBoard()
    """
    body = openapi_server.PrefsSelfJoin()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/selfJoin'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_prefs_voting_by_id_board(client):
    """Test case for update_boards_prefs_voting_by_id_board

    updateBoardsPrefsVotingByIdBoard()
    """
    body = openapi_server.PrefsVoting()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/prefs/voting'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_boards_subscribed_by_id_board(client):
    """Test case for update_boards_subscribed_by_id_board

    updateBoardsSubscribedByIdBoard()
    """
    body = openapi_server.BoardsSubscribed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/boards/{id_board}/subscribed'.format(id_board='id_board_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

