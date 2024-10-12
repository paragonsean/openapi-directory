# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate


pytestmark = pytest.mark.asyncio

async def test_oauth_access(client):
    """Test case for oauth_access

    
    """
    params = [('client_id', 'client_id_example'),
                    ('client_secret', 'client_secret_example'),
                    ('code', 'code_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('single_channel', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oauth.access',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_token(client):
    """Test case for oauth_token

    
    """
    params = [('client_id', 'client_id_example'),
                    ('client_secret', 'client_secret_example'),
                    ('code', 'code_example'),
                    ('redirect_uri', 'redirect_uri_example'),
                    ('single_channel', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oauth.token',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth_v2_access_0(client):
    """Test case for oauth_v2_access_0

    
    """
    params = [('client_id', 'client_id_example'),
                    ('client_secret', 'client_secret_example'),
                    ('code', 'code_example'),
                    ('redirect_uri', 'redirect_uri_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/oauth.v2.access',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

