# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rights import Rights


pytestmark = pytest.mark.asyncio

async def test_get_oauth_authorize_0(client):
    """Test case for get_oauth_authorize_0

    
    """
    params = [('oauth_token', 'oauth_token_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oauth_rights_0(client):
    """Test case for get_oauth_rights_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/oauth/rights',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_access_token_query_post_0(client):
    """Test case for oauth_access_token_query_post_0

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/access_token_query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_request_token_query_post_0(client):
    """Test case for oauth_request_token_query_post_0

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/request_token_query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_access_token_0(client):
    """Test case for post_oauth_access_token_0

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/access_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_authorize_0(client):
    """Test case for post_oauth_authorize_0

    
    """
    params = [('almighty', 'almighty_example'),
                    ('access_organisations', 'access_organisations_example'),
                    ('manage_organisations', 'manage_organisations_example'),
                    ('manage_organisations_services', 'manage_organisations_services_example'),
                    ('manage_organisations_applications', 'manage_organisations_applications_example'),
                    ('manage_organisations_members', 'manage_organisations_members_example'),
                    ('access_organisations_bills', 'access_organisations_bills_example'),
                    ('access_organisations_credit_count', 'access_organisations_credit_count_example'),
                    ('access_organisations_consumption_statistics', 'access_organisations_consumption_statistics_example'),
                    ('access_personal_information', 'access_personal_information_example'),
                    ('manage_personal_information', 'manage_personal_information_example'),
                    ('manage_ssh_keys', 'manage_ssh_keys_example'),
                    ('manage_services', 'manage_services_example'),
                    ('manage_applications', 'manage_applications_example'),
                    ('access_bills', 'access_bills_example'),
                    ('access_credit_count', 'access_credit_count_example'),
                    ('access_consumption_statistics', 'access_consumption_statistics_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_oauth_request_token_0(client):
    """Test case for post_oauth_request_token_0

    
    """
    params = [('oauth_consumer_key', 'oauth_consumer_key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('oauth_signature_method', 'oauth_signature_method_example'),
                    ('oauth_signature', 'oauth_signature_example'),
                    ('oauth_timestamp', 'oauth_timestamp_example'),
                    ('oauth_nonce', 'oauth_nonce_example'),
                    ('oauth_version', 'oauth_version_example'),
                    ('oauth_verifier', 'oauth_verifier_example'),
                    ('oauth_callback', 'oauth_callback_example'),
                    ('oauth_token_secret', 'oauth_token_secret_example'),
                    ('oauth_callback_confirmed', 'oauth_callback_confirmed_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/oauth/request_token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

