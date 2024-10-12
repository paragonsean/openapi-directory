# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.client import Client
from openapi_server.models.o_auth2_error import OAuth2Error
from openapi_server.models.problem_detail import ProblemDetail


pytestmark = pytest.mark.asyncio

async def test_client(client):
    """Test case for client

    List clients
    """
    headers = { 
        'Accept': 'application/json',
        'client_registration_token': 'special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/client',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_client_client_id(client):
    """Test case for client_client_id

    Delete a client
    """
    headers = { 
        'Accept': 'application/json',
        'client_registration_token': 'special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/client/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_client(client):
    """Test case for create_client

    Register a client
    """
    body = {"client_uri":"client_uri","default_max_age":0,"grant_types":["grant_types","grant_types"],"application_type":"application_type","logo_uri":"logo_uri","redirect_uris":["redirect_uris","redirect_uris"],"default_scopes":["default_scopes","default_scopes"],"client_id":"client_id","tos_uri":"tos_uri","client_name":"client_name","contacts":["contacts","contacts"],"policy_uri":"policy_uri","response_types":["response_types","response_types"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'client_registration_token': 'special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/client',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_client(client):
    """Test case for get_client

    View a client
    """
    headers = { 
        'Accept': 'application/json',
        'client_registration_token': 'special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/client/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_client(client):
    """Test case for update_client

    Update a client
    """
    body = {"client_uri":"client_uri","default_max_age":0,"grant_types":["grant_types","grant_types"],"application_type":"application_type","logo_uri":"logo_uri","redirect_uris":["redirect_uris","redirect_uris"],"default_scopes":["default_scopes","default_scopes"],"client_id":"client_id","tos_uri":"tos_uri","client_name":"client_name","contacts":["contacts","contacts"],"policy_uri":"policy_uri","response_types":["response_types","response_types"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'client_registration_token': 'special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/client/{client_id}'.format(client_id='client_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

