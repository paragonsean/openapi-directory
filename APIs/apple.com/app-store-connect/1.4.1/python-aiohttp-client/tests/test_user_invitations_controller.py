# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_response import AppsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.user_invitation_create_request import UserInvitationCreateRequest
from openapi_server.models.user_invitation_response import UserInvitationResponse
from openapi_server.models.user_invitations_response import UserInvitationsResponse


pytestmark = pytest.mark.asyncio

async def test_user_invitations_create_instance(client):
    """Test case for user_invitations_create_instance

    
    """
    body = {"data":{"relationships":{"visibleApps":{"data":[{"id":"id","type":"apps"},{"id":"id","type":"apps"}]}},"attributes":{"firstName":"firstName","lastName":"lastName","roles":["ADMIN","ADMIN"],"allAppsVisible":True,"email":"email","provisioningAllowed":True},"type":"userInvitations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/userInvitations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_invitations_delete_instance(client):
    """Test case for user_invitations_delete_instance

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/userInvitations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_invitations_get_collection(client):
    """Test case for user_invitations_get_collection

    
    """
    params = [('filter[email]', ['filter_email_example']),
                    ('filter[roles]', ['filter_roles_example']),
                    ('filter[visibleApps]', ['filter_visible_apps_example']),
                    ('sort', ['sort_example']),
                    ('fields[userInvitations]', ['fields_user_invitations_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[visibleApps]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/userInvitations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_invitations_get_instance(client):
    """Test case for user_invitations_get_instance

    
    """
    params = [('fields[userInvitations]', ['fields_user_invitations_example']),
                    ('include', ['include_example']),
                    ('fields[apps]', ['fields_apps_example']),
                    ('limit[visibleApps]', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/userInvitations/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_invitations_visible_apps_get_to_many_related(client):
    """Test case for user_invitations_visible_apps_get_to_many_related

    
    """
    params = [('fields[apps]', ['fields_apps_example']),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/userInvitations/{id}/visibleApps'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

