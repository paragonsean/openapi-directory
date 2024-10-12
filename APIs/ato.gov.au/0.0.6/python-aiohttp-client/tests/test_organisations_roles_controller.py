# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.party_role import PartyRole
from openapi_server.models.unauthenticated import Unauthenticated


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_roles_get(client):
    """Test case for organisations_party_id_roles_get

    Retrieve a list of roles
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations/{party_id}/roles'.format(party_id='party_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_roles_post(client):
    """Test case for organisations_party_id_roles_post

    Create a role
    """
    body = openapi_server.PartyRole()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/organisations/{party_id}/roles'.format(party_id='party_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_roles_role_id_delete(client):
    """Test case for organisations_party_id_roles_role_id_delete

    Delete a role
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/organisations/{party_id}/roles/{role_id}'.format(party_id='party_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_roles_role_id_get(client):
    """Test case for organisations_party_id_roles_role_id_get

    Retrieve a role
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/organisations/{party_id}/roles/{role_id}'.format(party_id='party_id_example', role_id='role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organisations_party_id_roles_role_id_put(client):
    """Test case for organisations_party_id_roles_role_id_put

    Update a role
    """
    body = openapi_server.PartyRole()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/organisations/{party_id}/roles/{role_id}'.format(party_id='party_id_example', role_id='role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

