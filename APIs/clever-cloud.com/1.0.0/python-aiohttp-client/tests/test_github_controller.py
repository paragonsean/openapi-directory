# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.key import Key
from openapi_server.models.transaction_id import TransactionId


pytestmark = pytest.mark.asyncio

async def test_delete_github_link_0(client):
    """Test case for delete_github_link_0

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/github/link',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_0(client):
    """Test case for get_github_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_applications_1(client):
    """Test case for get_github_applications_1

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/applications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_callback_0(client):
    """Test case for get_github_callback_0

    
    """
    params = [('code', 'code_example'),
                    ('state', 'state_example'),
                    ('error', 'error_example'),
                    ('error_description', 'error_description_example'),
                    ('error_uri', 'error_uri_example')]
    headers = { 
        'cookie': 'cookie_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/callback',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_emails_0(client):
    """Test case for get_github_emails_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/emails',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_keys_0(client):
    """Test case for get_github_keys_0

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/keys',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_link_0(client):
    """Test case for get_github_link_0

    
    """
    params = [('transactionId', 'transaction_id_example'),
                    ('redirectUrl', 'redirect_url_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/link',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_login_0(client):
    """Test case for get_github_login_0

    
    """
    params = [('redirectUrl', 'redirect_url_example'),
                    ('fromAuthorize', 'from_authorize_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/login',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_signup_0(client):
    """Test case for get_github_signup_0

    
    """
    params = [('redirectUrl', 'redirect_url_example'),
                    ('fromAuthorize', 'from_authorize_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v2/github/signup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_github_username_0(client):
    """Test case for get_github_username_0

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/github/username',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_github_redeploy_0(client):
    """Test case for post_github_redeploy_0

    
    """
    headers = { 
        'user_agent': 'user_agent_example',
        'x_github_event': 'x_github_event_example',
        'x_hub_signature': 'x_hub_signature_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/github/redeploy',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_github_signup_0(client):
    """Test case for post_github_signup_0

    
    """
    params = [('transactionId', 'transaction_id_example'),
                    ('name', 'name_example'),
                    ('otherId', 'other_id_example'),
                    ('otherEmail', 'other_email_example'),
                    ('password', 'password_example'),
                    ('autoLink', 'auto_link_example'),
                    ('terms', 'terms_example')]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/v2/github/signup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

