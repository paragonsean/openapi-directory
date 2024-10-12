# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_api_oauth_authorize_post(client):
    """Test case for api_oauth_authorize_post

    
    """
    params = [('client_id', 'client_id_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('state', 'state_example'),
                    ('scope', 'scope_example'),
                    ('client_secret', 'client_secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_o_auth_authorize(client):
    """Test case for o_auth_authorize

    
    """
    params = [('client_id', 'client_id_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('state', 'state_example'),
                    ('scope', 'scope_example'),
                    ('client_secret', 'client_secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/oauth/authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

