# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.allowed_origin import AllowedOrigin
from openapi_server.models.allowed_origins_response import AllowedOriginsResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(client):
    """Test case for delete_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

    Delete an allowed origin
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}/allowedOrigins/{origin_id}'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example', origin_id='origin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(client):
    """Test case for get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

    Get a list of allowed origins
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}/allowedOrigins'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id(client):
    """Test case for get_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins_origin_id

    Get an allowed origin
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}/allowedOrigins/{origin_id}'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example', origin_id='origin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins(client):
    """Test case for post_merchants_merchant_id_api_credentials_api_credential_id_allowed_origins

    Create an allowed origin
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
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}/allowedOrigins'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

