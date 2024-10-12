# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.lists import Lists
from openapi_server.models.lists_cards import ListsCards
from openapi_server.models.lists_closed import ListsClosed
from openapi_server.models.lists_id_board import ListsIdBoard
from openapi_server.models.lists_move_all_cards import ListsMoveAllCards
from openapi_server.models.lists_name import ListsName
from openapi_server.models.lists_pos import ListsPos
from openapi_server.models.lists_subscribed import ListsSubscribed


pytestmark = pytest.mark.asyncio

async def test_add_lists(client):
    """Test case for add_lists

    addLists()
    """
    body = openapi_server.Lists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/lists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_lists_archive_all_cards_by_id_list(client):
    """Test case for add_lists_archive_all_cards_by_id_list

    addListsArchiveAllCardsByIdList()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/lists/{id_list}/archiveAllCards'.format(id_list='id_list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_lists_cards_by_id_list(client):
    """Test case for add_lists_cards_by_id_list

    addListsCardsByIdList()
    """
    body = openapi_server.ListsCards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/lists/{id_list}/cards'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_lists_move_all_cards_by_id_list(client):
    """Test case for add_lists_move_all_cards_by_id_list

    addListsMoveAllCardsByIdList()
    """
    body = openapi_server.ListsMoveAllCards()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/lists/{id_list}/moveAllCards'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_actions_by_id_list(client):
    """Test case for get_lists_actions_by_id_list

    getListsActionsByIdList()
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
        path='/1/lists/{id_list}/actions'.format(id_list='id_list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_board_by_id_list(client):
    """Test case for get_lists_board_by_id_list

    getListsBoardByIdList()
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
        path='/1/lists/{id_list}/board'.format(id_list='id_list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_board_by_id_list_by_field(client):
    """Test case for get_lists_board_by_id_list_by_field

    getListsBoardByIdListByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/lists/{id_list}/board/{_field}'.format(id_list='id_list_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_by_id_list(client):
    """Test case for get_lists_by_id_list

    getListsByIdList()
    """
    params = [('cards', 'none'),
                    ('card_fields', 'all'),
                    ('board', 'board_example'),
                    ('board_fields', 'name, desc, descData, closed, idOrganization, pinned, url and prefs'),
                    ('fields', 'name, closed, idBoard and pos'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/lists/{id_list}'.format(id_list='id_list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_by_id_list_by_field(client):
    """Test case for get_lists_by_id_list_by_field

    getListsByIdListByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/lists/{id_list}/{_field}'.format(id_list='id_list_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_cards_by_id_list(client):
    """Test case for get_lists_cards_by_id_list

    getListsCardsByIdList()
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
        path='/1/lists/{id_list}/cards'.format(id_list='id_list_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_cards_by_id_list_by_filter(client):
    """Test case for get_lists_cards_by_id_list_by_filter

    getListsCardsByIdListByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/lists/{id_list}/cards/{filter}'.format(id_list='id_list_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_by_id_list(client):
    """Test case for update_lists_by_id_list

    updateListsByIdList()
    """
    body = openapi_server.Lists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_closed_by_id_list(client):
    """Test case for update_lists_closed_by_id_list

    updateListsClosedByIdList()
    """
    body = openapi_server.ListsClosed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}/closed'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_id_board_by_id_list(client):
    """Test case for update_lists_id_board_by_id_list

    updateListsIdBoardByIdList()
    """
    body = openapi_server.ListsIdBoard()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}/idBoard'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_name_by_id_list(client):
    """Test case for update_lists_name_by_id_list

    updateListsNameByIdList()
    """
    body = openapi_server.ListsName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}/name'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_pos_by_id_list(client):
    """Test case for update_lists_pos_by_id_list

    updateListsPosByIdList()
    """
    body = openapi_server.ListsPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}/pos'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_lists_subscribed_by_id_list(client):
    """Test case for update_lists_subscribed_by_id_list

    updateListsSubscribedByIdList()
    """
    body = openapi_server.ListsSubscribed()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/lists/{id_list}/subscribed'.format(id_list='id_list_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

