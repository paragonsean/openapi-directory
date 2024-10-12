# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_credential import ApiCredential
from openapi_server.models.create_api_credential_response import CreateApiCredentialResponse
from openapi_server.models.create_merchant_api_credential_request import CreateMerchantApiCredentialRequest
from openapi_server.models.list_merchant_api_credentials_response import ListMerchantApiCredentialsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.update_merchant_api_credential_request import UpdateMerchantApiCredentialRequest


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_api_credentials(client):
    """Test case for get_merchants_merchant_id_api_credentials

    Get a list of API credentials
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/apiCredentials'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_api_credentials_api_credential_id(client):
    """Test case for get_merchants_merchant_id_api_credentials_api_credential_id

    Get an API credential
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_api_credentials_api_credential_id(client):
    """Test case for patch_merchants_merchant_id_api_credentials_api_credential_id

    Update an API credential
    """
    body = {"allowedOrigins":["allowedOrigins","allowedOrigins"],"roles":["roles","roles"],"active":True,"description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/apiCredentials/{api_credential_id}'.format(merchant_id='merchant_id_example', api_credential_id='api_credential_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_api_credentials(client):
    """Test case for post_merchants_merchant_id_api_credentials

    Create an API credential
    """
    body = {"allowedOrigins":["allowedOrigins","allowedOrigins"],"roles":["roles","roles"],"description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/apiCredentials'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

