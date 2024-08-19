# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.checklists import Checklists
from openapi_server.models.checklists_check_items import ChecklistsCheckItems
from openapi_server.models.checklists_id_card import ChecklistsIdCard
from openapi_server.models.checklists_name import ChecklistsName
from openapi_server.models.checklists_pos import ChecklistsPos


pytestmark = pytest.mark.asyncio

async def test_add_checklists(client):
    """Test case for add_checklists

    addChecklists()
    """
    body = openapi_server.Checklists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/checklists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_checklists_check_items_by_id_checklist(client):
    """Test case for add_checklists_check_items_by_id_checklist

    addChecklistsCheckItemsByIdChecklist()
    """
    body = openapi_server.ChecklistsCheckItems()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/1/checklists/{id_checklist}/checkItems'.format(id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_checklists_by_id_checklist(client):
    """Test case for delete_checklists_by_id_checklist

    deleteChecklistsByIdChecklist()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/checklists/{id_checklist}'.format(id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_checklists_check_items_by_id_checklist_by_id_check_item(client):
    """Test case for delete_checklists_check_items_by_id_checklist_by_id_check_item

    deleteChecklistsCheckItemsByIdChecklistByIdCheckItem()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/checklists/{id_checklist}/checkItems/{id_check_item}'.format(id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_board_by_id_checklist(client):
    """Test case for get_checklists_board_by_id_checklist

    getChecklistsBoardByIdChecklist()
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
        path='/1/checklists/{id_checklist}/board'.format(id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_board_by_id_checklist_by_field(client):
    """Test case for get_checklists_board_by_id_checklist_by_field

    getChecklistsBoardByIdChecklistByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}/board/{_field}'.format(id_checklist='id_checklist_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_by_id_checklist(client):
    """Test case for get_checklists_by_id_checklist

    getChecklistsByIdChecklist()
    """
    params = [('cards', 'none'),
                    ('card_fields', 'all'),
                    ('checkItems', 'all'),
                    ('checkItem_fields', 'name, nameData, pos and state'),
                    ('fields', 'all'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}'.format(id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_by_id_checklist_by_field(client):
    """Test case for get_checklists_by_id_checklist_by_field

    getChecklistsByIdChecklistByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}/{_field}'.format(id_checklist='id_checklist_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_cards_by_id_checklist(client):
    """Test case for get_checklists_cards_by_id_checklist

    getChecklistsCardsByIdChecklist()
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
        path='/1/checklists/{id_checklist}/cards'.format(id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_cards_by_id_checklist_by_filter(client):
    """Test case for get_checklists_cards_by_id_checklist_by_filter

    getChecklistsCardsByIdChecklistByFilter()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}/cards/{filter}'.format(id_checklist='id_checklist_example', filter='filter_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_check_items_by_id_checklist(client):
    """Test case for get_checklists_check_items_by_id_checklist

    getChecklistsCheckItemsByIdChecklist()
    """
    params = [('filter', 'all'),
                    ('fields', 'name, nameData, pos and state'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}/checkItems'.format(id_checklist='id_checklist_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_checklists_check_items_by_id_checklist_by_id_check_item(client):
    """Test case for get_checklists_check_items_by_id_checklist_by_id_check_item

    getChecklistsCheckItemsByIdChecklistByIdCheckItem()
    """
    params = [('fields', 'name, nameData, pos and state'),
                    ('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/checklists/{id_checklist}/checkItems/{id_check_item}'.format(id_checklist='id_checklist_example', id_check_item='id_check_item_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_checklists_by_id_checklist(client):
    """Test case for update_checklists_by_id_checklist

    updateChecklistsByIdChecklist()
    """
    body = openapi_server.Checklists()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/checklists/{id_checklist}'.format(id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_checklists_id_card_by_id_checklist(client):
    """Test case for update_checklists_id_card_by_id_checklist

    updateChecklistsIdCardByIdChecklist()
    """
    body = openapi_server.ChecklistsIdCard()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/checklists/{id_checklist}/idCard'.format(id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_checklists_name_by_id_checklist(client):
    """Test case for update_checklists_name_by_id_checklist

    updateChecklistsNameByIdChecklist()
    """
    body = openapi_server.ChecklistsName()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/checklists/{id_checklist}/name'.format(id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_checklists_pos_by_id_checklist(client):
    """Test case for update_checklists_pos_by_id_checklist

    updateChecklistsPosByIdChecklist()
    """
    body = openapi_server.ChecklistsPos()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/checklists/{id_checklist}/pos'.format(id_checklist='id_checklist_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

