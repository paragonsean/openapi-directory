# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collaborator import Collaborator
from openapi_server.models.collaborator_editable import CollaboratorEditable


pytestmark = pytest.mark.asyncio

async def test_maps_id_collaborators_get(client):
    """Test case for maps_id_collaborators_get

    List collaborators of a map
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/maps/{id}/collaborators'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_collaborators_user_id_delete(client):
    """Test case for maps_id_collaborators_user_id_delete

    Delete collaboration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/maps/{id}/collaborators/{user_id}'.format(id=56, user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_maps_id_collaborators_user_id_patch(client):
    """Test case for maps_id_collaborators_user_id_patch

    Update collaborator
    """
    collaborator = {"group":"editor"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/maps/{id}/collaborators/{user_id}'.format(id=56, user_id=56),
        headers=headers,
        json=collaborator,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

