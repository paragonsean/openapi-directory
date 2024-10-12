# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invitation import Invitation
from openapi_server.models.invitation_read import InvitationRead
from openapi_server.models.invitation_write import InvitationWrite


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_accept_invitation_item(client):
    """Test case for accept_invitation_item

    Creates a Invitation resource.
    """
    invitation = {"createdAt":"2000-01-23T04:56:07.000+00:00","id":"id","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/invitations/accept/{token}'.format(token='token_example'),
        headers=headers,
        json=invitation,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_invitation_item(client):
    """Test case for delete_invitation_item

    Removes the Invitation resource.
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/invitations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invitation_collection(client):
    """Test case for get_invitation_collection

    Retrieves the collection of Invitation resources.
    """
    params = [('targetId', 'target_id_example'),
                    ('targetType', 'target_type_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/invitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invitation_item(client):
    """Test case for get_invitation_item

    Retrieves a Invitation resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/invitations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_invitation_collection(client):
    """Test case for post_invitation_collection

    Creates a Invitation resource.
    """
    invitation = openapi_server.InvitationWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/invitations',
        headers=headers,
        json=invitation,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

