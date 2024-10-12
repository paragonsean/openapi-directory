# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collaborator_invitation import CollaboratorInvitation
from openapi_server.models.collaborator_invitation_create import CollaboratorInvitationCreate


pytestmark = pytest.mark.asyncio

async def test_collaborator_invitations_get(client):
    """Test case for collaborator_invitations_get

    List your collaborator invitations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/collaborator_invitations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collaborator_invitations_id_delete(client):
    """Test case for collaborator_invitations_id_delete

    Delete collaborator invitation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/collaborator_invitations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collaborator_invitations_id_get(client):
    """Test case for collaborator_invitations_id_get

    Show collaborator invitation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/collaborator_invitations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collaborator_invitations_id_patch(client):
    """Test case for collaborator_invitations_id_patch

    Accept collaborator invitation.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/collaborator_invitations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collaborator_invitations_post(client):
    """Test case for collaborator_invitations_post

    Invite user to collaborate on map
    """
    body = {"emails":"a@b.com, c@d.com, e@f.com","is_admin":True,"map_id":34925783,"user_ids":"5839459, 389423, 89494, 686950"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/collaborator_invitations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

