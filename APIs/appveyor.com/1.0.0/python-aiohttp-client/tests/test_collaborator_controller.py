# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collaborator_update import CollaboratorUpdate
from openapi_server.models.error import Error
from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_roles_results import UserAccountRolesResults


pytestmark = pytest.mark.asyncio

async def test_delete_collaborator(client):
    """Test case for delete_collaborator

    Delete collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/collaborators/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collaborator(client):
    """Test case for get_collaborator

    Get collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/collaborators/{user_id}'.format(user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collaborators(client):
    """Test case for get_collaborators

    Get collaborators
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/collaborators',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_collaborator(client):
    """Test case for update_collaborator

    Update collaborator
    """
    body = {"roleId":3040,"userId":2018}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/collaborators',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

