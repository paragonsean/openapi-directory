# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server.models.create_token_request import CreateTokenRequest
from openapi_server.models.create_token_response import CreateTokenResponse
from openapi_server.models.fetch_error_response import FetchErrorResponse
from openapi_server.models.fetch_groups_response import FetchGroupsResponse
from openapi_server.models.fetch_organization_response import FetchOrganizationResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_token(client):
    """Test case for create_token

    Create an oauth token
    """
    body = {"data":{"attributes":{"client_id":"95c78ab2-167f-40b8-8bec-8398d4b87454","client_secret":"35d18dc9-a3dd-4948-b787-063a490b9354","grant_type":"client_credentials"},"type":"oauth/token"}}
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/pub/oauth/token',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_token_groups(client):
    """Test case for fetch_token_groups

    Get the groups for a token
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/pub/oauth/token/{id}/groups'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_token_organization(client):
    """Test case for fetch_token_organization

    Get the organization for a token
    """
    headers = { 
        'Accept': 'application/vnd.api+json',
    }
    response = await client.request(
        method='GET',
        path='/pub/oauth/token/{id}/organization'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

