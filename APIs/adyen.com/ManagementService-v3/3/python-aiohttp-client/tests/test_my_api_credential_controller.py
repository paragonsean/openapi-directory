# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.allowed_origin import AllowedOrigin
from openapi_server.models.allowed_origins_response import AllowedOriginsResponse
from openapi_server.models.create_allowed_origin_request import CreateAllowedOriginRequest
from openapi_server.models.generate_client_key_response import GenerateClientKeyResponse
from openapi_server.models.me_api_credential import MeApiCredential
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_delete_me_allowed_origins_origin_id(client):
    """Test case for delete_me_allowed_origins_origin_id

    Remove allowed origin
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/me/allowedOrigins/{origin_id}'.format(origin_id='origin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me(client):
    """Test case for get_me

    Get API credential details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me_allowed_origins(client):
    """Test case for get_me_allowed_origins

    Get allowed origins
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/me/allowedOrigins',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_me_allowed_origins_origin_id(client):
    """Test case for get_me_allowed_origins_origin_id

    Get allowed origin details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/me/allowedOrigins/{origin_id}'.format(origin_id='origin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_me_allowed_origins(client):
    """Test case for post_me_allowed_origins

    Add allowed origin
    """
    body = {"_links":{"self":{"href":"href"}},"domain":"domain","id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/me/allowedOrigins',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_me_generate_client_key(client):
    """Test case for post_me_generate_client_key

    Generate a client key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/me/generateClientKey',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

