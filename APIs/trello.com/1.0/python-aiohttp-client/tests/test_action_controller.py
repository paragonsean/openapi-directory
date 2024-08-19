# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actions import Actions
from openapi_server.models.actions_text import ActionsText


pytestmark = pytest.mark.asyncio

async def test_delete_actions_by_id_action(client):
    """Test case for delete_actions_by_id_action

    deleteActionsByIdAction()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/1/actions/{id_action}'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_board_by_id_action(client):
    """Test case for get_actions_board_by_id_action

    getActionsBoardByIdAction()
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
        path='/1/actions/{id_action}/board'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_board_by_id_action_by_field(client):
    """Test case for get_actions_board_by_id_action_by_field

    getActionsBoardByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/board/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_by_id_action(client):
    """Test case for get_actions_by_id_action

    getActionsByIdAction()
    """
    params = [('display', 'display_example'),
                    ('entities', 'entities_example'),
                    ('fields', 'all'),
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
        path='/1/actions/{id_action}'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_by_id_action_by_field(client):
    """Test case for get_actions_by_id_action_by_field

    getActionsByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_card_by_id_action(client):
    """Test case for get_actions_card_by_id_action

    getActionsCardByIdAction()
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
        path='/1/actions/{id_action}/card'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_card_by_id_action_by_field(client):
    """Test case for get_actions_card_by_id_action_by_field

    getActionsCardByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/card/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_display_by_id_action(client):
    """Test case for get_actions_display_by_id_action

    getActionsDisplayByIdAction()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/display'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_entities_by_id_action(client):
    """Test case for get_actions_entities_by_id_action

    getActionsEntitiesByIdAction()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/entities'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_list_by_id_action(client):
    """Test case for get_actions_list_by_id_action

    getActionsListByIdAction()
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
        path='/1/actions/{id_action}/list'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_list_by_id_action_by_field(client):
    """Test case for get_actions_list_by_id_action_by_field

    getActionsListByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/list/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_member_by_id_action(client):
    """Test case for get_actions_member_by_id_action

    getActionsMemberByIdAction()
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
        path='/1/actions/{id_action}/member'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_member_by_id_action_by_field(client):
    """Test case for get_actions_member_by_id_action_by_field

    getActionsMemberByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/member/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_member_creator_by_id_action(client):
    """Test case for get_actions_member_creator_by_id_action

    getActionsMemberCreatorByIdAction()
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
        path='/1/actions/{id_action}/memberCreator'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_member_creator_by_id_action_by_field(client):
    """Test case for get_actions_member_creator_by_id_action_by_field

    getActionsMemberCreatorByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/memberCreator/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_organization_by_id_action(client):
    """Test case for get_actions_organization_by_id_action

    getActionsOrganizationByIdAction()
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
        path='/1/actions/{id_action}/organization'.format(id_action='id_action_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actions_organization_by_id_action_by_field(client):
    """Test case for get_actions_organization_by_id_action_by_field

    getActionsOrganizationByIdActionByField()
    """
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/1/actions/{id_action}/organization/{_field}'.format(id_action='id_action_example', _field='_field_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_actions_by_id_action(client):
    """Test case for update_actions_by_id_action

    updateActionsByIdAction()
    """
    body = openapi_server.Actions()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/actions/{id_action}'.format(id_action='id_action_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_actions_text_by_id_action(client):
    """Test case for update_actions_text_by_id_action

    updateActionsTextByIdAction()
    """
    body = openapi_server.ActionsText()
    params = [('key', 'key_example'),
                    ('token', 'token_example')]
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'api_token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/1/actions/{id_action}/text'.format(id_action='id_action_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

