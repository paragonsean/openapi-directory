# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_role_credentials_response import GetRoleCredentialsResponse
from openapi_server.models.list_account_roles_response import ListAccountRolesResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse


pytestmark = pytest.mark.asyncio

async def test_get_role_credentials(client):
    """Test case for get_role_credentials

    
    """
    params = [('role_name', 'role_name_example'),
                    ('account_id', 'account_id_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_sso_bearer_token': 'x_amz_sso_bearer_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/federation/credentials#role_name&account_id&x-amz-sso_bearer_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_account_roles(client):
    """Test case for list_account_roles

    
    """
    params = [('next_token', 'next_token_example'),
                    ('max_result', 56),
                    ('account_id', 'account_id_example'),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_sso_bearer_token': 'x_amz_sso_bearer_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/assignment/roles#x-amz-sso_bearer_token&account_id',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_accounts(client):
    """Test case for list_accounts

    
    """
    params = [('next_token', 'next_token_example'),
                    ('max_result', 56),
                    ('maxResults', 'max_results_example'),
                    ('nextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_sso_bearer_token': 'x_amz_sso_bearer_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/assignment/accounts#x-amz-sso_bearer_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_sso_bearer_token': 'x_amz_sso_bearer_token_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/logout#x-amz-sso_bearer_token',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

